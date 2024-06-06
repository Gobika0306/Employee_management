from django.db import models
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
import datetime


# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Activity(models.Model):
    emp = models.ForeignKey(Emp, on_delete=models.CASCADE)     
    activity_name = models.CharField(max_length=100)
    plan_start = models.DateField()
    plan_duration = models.IntegerField()
    actual_start = models.DateField(null=True, blank=True)
    actual_duration = models.IntegerField(null=True, blank=True)
    
    @property
    def percent_complete(self):
        if self.actual_start and self.actual_duration:
            # Calculate the actual end date based on actual start and duration
            actual_end_date = self.actual_start + datetime.timedelta(days=self.actual_duration)
            # Calculate the plan end date based on plan start and duration
            plan_end_date = self.plan_start + datetime.timedelta(days=self.plan_duration)
            today = datetime.date.today()

            # If the actual end date is in the past or today, the task is complete
            if actual_end_date <= today:
                return 100

            # If the task is not completed yet, calculate elapsed actual days
            elapsed_actual_days = (today - self.actual_start).days

            # Calculate the percentage of completion based on elapsed actual days and planned duration
            percent_complete = (elapsed_actual_days / self.plan_duration) * 100

            # Ensure the percentage is between 0 and 100
            return max(min(percent_complete, 100), 0)
        elif self.actual_start:
            # If actual duration is not set but actual start is set, calculate elapsed actual days
            elapsed_actual_days = (datetime.date.today() - self.actual_start).days
            percent_complete = (elapsed_actual_days / self.plan_duration) * 100
            return max(min(percent_complete, 100), 0)
        else:
            return 0

    def __str__(self):
        return self.activity_name
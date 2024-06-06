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
            # Calculate the elapsed time since actual start
            elapsed_actual_days = (datetime.date.today() - self.actual_start).days
            # Calculate the elapsed time since plan start
            elapsed_plan_days = (datetime.date.today() - self.plan_start).days
            # Calculate the expected duration
            expected_duration = self.plan_duration
            # Calculate the percentage of completion
            if elapsed_actual_days <= expected_duration:
                percent_complete = (elapsed_actual_days / expected_duration) * 100
            else:
                percent_complete = 100
            return min(percent_complete, 100)  # Ensure the percentage is not greater than 100
        else:
            return 0

    def __str__(self):
        return self.name
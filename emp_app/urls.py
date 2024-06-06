from django.contrib import admin
from django.urls import path,include
from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path("home/",emp_home),
    path("add-emp/",add_emp),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("update-emp/<int:emp_id>",update_emp),
    path("do-update-emp/<int:emp_id>",do_update_emp),
    # path('emp/activity/<int:emp_id>/', views.emp_activity, name='emp_activity'),
    # path('activities/emp/<int:emp_id>/create/', views.activity_create, name='activity_create'),
    path('activities/emp/<int:emp_id>/', views.activity_list_by_emp, name='activity_by_emp'),
    path('activities/emp/<int:emp_id>/create/', views.activity_create, name='activity_create'),
    path('activities/emp/<int:emp_id>/update/<int:activity_id>/', views.activity_update, name='activity_update'),
    path('activities/emp/<int:emp_id>/delete/<int:activity_id>/', views.activity_delete, name='activity_delete'),

]

    # Other URL patterns...


   


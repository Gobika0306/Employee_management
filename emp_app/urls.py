from django.contrib import admin
from django.urls import path,include
from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('home/', views.emp_home, name='home'),
    path('add-emp/', views.add_emp, name='add_emp'),
    path('delete-emp/<int:emp_id>/', views.delete_emp, name='delete_emp'),
    path('update-emp/<int:emp_id>/', views.update_emp, name='update_emp'),
    path('do-update-emp/<int:emp_id>/', views.do_update_emp, name='do_update_emp'),
    path('activities/emp/<int:emp_id>/', views.activity_list_by_emp, name='activity_by_emp'),
    path('activities/emp/<int:emp_id>/create/', views.activity_create, name='activity_create'),
    path('activities/emp/<int:emp_id>/update/<int:activity_id>/', views.activity_update, name='activity_update'),
    path('activities/emp/<int:emp_id>/delete/<int:activity_id>/', views.activity_delete, name='activity_delete'),
]


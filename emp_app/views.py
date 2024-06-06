from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Emp
from django.shortcuts import render, get_object_or_404
from .models import Activity
from django.shortcuts import render, get_object_or_404, redirect
from .models import Activity, Emp
from .forms import ActivityForm




def emp_home(request):
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{'emps':emps})


def add_emp(request):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    print("Yes Bhai")
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })

def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=Emp.objects.get(pk=emp_id)

        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
    return redirect("/emp/home/")




# Other views...

def activity_list_by_emp(request, emp_id):
    emp = get_object_or_404(Emp, pk=emp_id)
    activities = Activity.objects.filter(emp=emp)
    return render(request, 'activity_list_by_emp.html', {'activities': activities, 'emp': emp})


# Create a new Activity
def activity_create(request, emp_id):
    emp = get_object_or_404(Emp, id=emp_id)
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.emp = emp
            activity.save()
            return redirect('activity_by_emp', emp_id=emp_id)  # Redirect to a success page or list of activities
    else:
        form = ActivityForm()
    return render(request, 'activity_form.html', {'form': form, 'emp': emp})


# Update an existing Activity
def activity_update(request, emp_id, activity_id):
    emp = get_object_or_404(Emp, pk=emp_id)
    activity = get_object_or_404(Activity, pk=activity_id)
    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activity_by_emp', emp_id=emp.id)
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'activity_form.html', {'form': form, 'emp': emp})

# Delete an Activity
def activity_delete(request, emp_id, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    emp = get_object_or_404(Emp, pk=emp_id)
    if request.method == "POST":
        activity.delete()
        return redirect('activity_by_emp', emp_id=emp.id)
    return render(request, 'activity_confirm_delete.html', {'activity': activity, 'emp': emp})
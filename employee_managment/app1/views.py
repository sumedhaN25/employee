from django.shortcuts import render, HttpResponse, redirect,  get_object_or_404
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q


# Create your views here.

def index_page(request):
    return render(request, 'index.html')


def view_emp(request):
    emp = Employee.objects.all()
    context = {
        'emp': emp
    }
    print(context)
    return render(request, 'view.html', context)


def add_emp(request):
    if request.method =='POST':
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        Department = request.POST['Department']
        salary = request.POST['Salary']
        role = request.POST['role']
        phone = int(request.POST['phone'])
        Hire_date = request.POST['Hire_date']
        new_emp = Employee(First_name=First_name, Last_name=Last_name, Dept_id=Department, Salary=salary, role_id=role, phone=phone, Hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added successfully...')
        # return redirect('add_emp')
    elif request.method == 'GET':
        return render(request, 'add.html')
    else:
        return HttpResponse("Exception Ocured")
    


def remove_emp(request, pk=None):
    if pk:
        try: 
            emp_to_be_removed = Employee.objects.get(id=pk)
            emp_to_be_removed.delete()
            # return HttpResponse("Employee removed Successfully...")
            return redirect('remove_emp')
        except:
            return("plz enter valid Id")
    emp = Employee.objects.all()
    context = {
        'emp': emp
    }
    return render(request, 'remove.html', context)




def fliter_emp(request):
    if request.method =='POST':
        name = request.POST.get('First_name')
        Dept = request.POST.get('Department')
        role = request.POST.get('role')
        emp = Employee.objects.all()
        if name:
            emp = emp.filter(Q(First_name__icontains=name))
        if Dept:
            emp = emp.filter(Q(Department__name = Dept))
        if role:
            emp = emp.filter(Q(role__name=role))

        context = {'emp': emp}
        return render(request, 'view.html', context)
    elif request.method== 'GET':

        return render(request, 'fliter.html')

    else:
        return HttpResponse('An ERROR')


    
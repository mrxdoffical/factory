from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Employee, session, Users

def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_employees')
        else:
            return render(request, 'login.html', {'error':'invalid credentials'})
    return render(request, 'login.html')


@login_required
def list_employees(request):
    employees = session.query(Employee).all()
    return render(request, 'employees/list.html', {'employees': employees})


@login_required
def add_employee(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = int(request.POST['age'])
        pay = int(request.POST['pay'])
        email = request.POST.get('email', f"{firstname}{lastname}@gmail.com")
        emp = Employee(firstname=firstname, lastname=lastname, age=age, pay=pay, email=email)
        session.add(emp)
        session.commit()
        return redirect('list_employees')
    return render(request, 'employees/add.html')

@login_required
def delete_employee(request, email):
    user = session.query(Employee).filter(Employee.email == email).first()
    if user:
        session.delete(user)
        session.commit()
        return redirect('list_employees')
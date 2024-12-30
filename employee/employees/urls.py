from django.urls import path, include
from .views import list_employees, add_employee, delete_employee

urlpatterns = [
	path('', list_employees, name='list_employees'),
	path('add/', add_employee, name='add_employee'),
	path('delete/<str:email>/', delete_employee, name='delete_employee'),
]
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import TEmployees, TDepartments
from.forms import EmpForm, DepForm

class PruebaView(TemplateView):
    template_name='home.html'

class EmployeeListView(ListView):
    template_name = "list.employees.html"
    model = TEmployees
    context_object_name = 'listE'

class DepartmentsListView(ListView):
    template_name = "list.departments.html"
    model = TDepartments
    context_object_name = 'listD'

class EmployeesCreateView(CreateView):
    model = TEmployees
    context_object_name = '/addE'
    template_name = "add.employee.html"
    form_class = EmpForm
    success_url = '/listE'

class DepartmentsCreateView(CreateView):
    model = TDepartments
    context_object_name = '/addD'
    template_name = "add.department.html"
    form_class = DepForm
    success_url = '/listD'

class EmployeesUpdateView(UpdateView):
    model = TEmployees
    template_name = "update.employees.html"
    fields=('__all__')
    success_url = '/listE'

class DepartmentsUpdateView(UpdateView):
    model = TDepartments
    template_name = "update.departments.html"
    fields=('__all__')
    success_url = '/listD'

class EmployeesDeleteView(DeleteView):
    model = TEmployees
    template_name = "delete.employees.html"
    fields=('__all__')
    success_url = '/listE'

class DepartmentsDeleteView(DeleteView):
    model = TDepartments
    template_name = "delete.departments.html"
    fields=('__all__')
    success_url = '/listD'
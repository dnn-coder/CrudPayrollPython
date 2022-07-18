from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('listE/', views.EmployeeListView.as_view()),
    path('listD/', views.DepartmentsListView.as_view()),
    path('addE/', views.EmployeesCreateView.as_view()),
    path('addD/', views.DepartmentsCreateView.as_view()),
    path('updateE/<pk>/', views.EmployeesUpdateView.as_view()),
    path('updateD/<pk>/', views.DepartmentsUpdateView.as_view()),
    path('deleteE/<pk>/', views.EmployeesDeleteView.as_view()),
    path('deleteD/<pk>/', views.DepartmentsDeleteView.as_view()),
]
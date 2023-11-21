from django.urls import path

from aplicatie2 import views

app_name = 'aplicatie2'

urlpatterns = [
    path('', views.CompaniesView.as_view(), name='lista_companii'),
    path('adaugare/', views.CreateCompanies.as_view(), name='adaugare'),
    path('<int:pk>/modificare/', views.UpdateCompanies.as_view(), name='modifica'),

]

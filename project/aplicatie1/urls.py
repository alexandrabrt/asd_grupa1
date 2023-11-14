from django.urls import path

from aplicatie1 import views

app_name = 'aplicatie1'

urlpatterns = [
    path('', views.LocationView.as_view(), name='lista_locatii'),
    path('adaugare/', views.CreateLocationView.as_view(), name='adaugare'),
]

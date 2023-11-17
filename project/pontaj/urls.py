from django.urls import path

from pontaj import views

app_name = 'pontaj'

urlpatterns = [
    path('start_pontaj/', views.new_timesheet, name='start_pontaj'),
    path('stop_pontaj/', views.stop_timesheet, name='stop_pontaj'),
]

from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    # Пока оставляем пустым или добавляем базовые URL
    path('', views.appointment_list, name='list'),
    path('create/', views.create_appointment, name='create'),
    path('<int:pk>/', views.appointment_detail, name='detail'),
]

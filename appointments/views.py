from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment

@login_required
def appointment_list(request):
    """Список записей"""
    return render(request, 'appointments/list.html', {
        'title': 'Мои записи'
    })

@login_required
def create_appointment(request):
    """Создание новой записи"""
    return render(request, 'appointments/create.html', {
        'title': 'Запись на прием'
    })

@login_required
def appointment_detail(request, pk):
    """Детали записи"""
    return render(request, 'appointments/detail.html', {
        'title': 'Детали записи'
    })

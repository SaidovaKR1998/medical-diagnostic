from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Appointment, Doctor
from services.models import Service
from accounts.models import CustomUser


@login_required
def create_appointment(request):
    """Создание новой записи на прием"""
    services = Service.objects.filter(is_active=True)
    doctors = Doctor.objects.filter(is_active=True)

    # Получаем service_id из параметра URL если есть
    selected_service_id = request.GET.get('service')

    if request.method == 'POST':
        try:
            # Получаем данные из формы
            service_id = request.POST.get('service')
            doctor_id = request.POST.get('doctor')
            appointment_date = request.POST.get('appointment_date')
            appointment_time = request.POST.get('appointment_time')
            notes = request.POST.get('notes', '')

            # Валидация
            if not all([service_id, appointment_date, appointment_time]):
                messages.error(request, 'Заполните все обязательные поля')
                return redirect('appointments:create')

            # Получаем объекты
            service = Service.objects.get(id=service_id, is_active=True)
            doctor = None
            if doctor_id:
                doctor = Doctor.objects.get(id=doctor_id, is_active=True)

            # Создаем запись
            appointment = Appointment.objects.create(
                patient=request.user,
                doctor=doctor,
                service=service,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                notes=notes,
                status='pending'
            )

            messages.success(request,
                             f'Запись на {appointment_date} в {appointment_time} создана! ' +
                             'Мы свяжемся с вами для подтверждения.')
            return redirect('appointments:list')

        except Service.DoesNotExist:
            messages.error(request, 'Услуга не найдена')
        except Doctor.DoesNotExist:
            messages.error(request, 'Врач не найден')
        except Exception as e:
            messages.error(request, f'Ошибка при создании записи: {str(e)}')

    context = {
        'title': 'Запись на прием',
        'services': services,
        'doctors': doctors,
        'selected_service_id': selected_service_id,
        'today': timezone.now().date().isoformat(),
    }
    return render(request, 'appointments/create.html', context)

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

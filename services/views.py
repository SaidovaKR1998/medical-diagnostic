from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Service, ServiceCategory


def service_list(request):
    """Список всех услуг"""
    categories = ServiceCategory.objects.all().prefetch_related('services')
    context = {
        'title': 'Наши услуги',
        'categories': categories,
    }
    return render(request, 'services/list.html', context)


def service_detail(request, slug):
    """Детальная информация об услуге"""
    service = get_object_or_404(Service, slug=slug, is_active=True)

    # Получаем похожие услуги из той же категории
    similar_services = Service.objects.filter(
        category=service.category,
        is_active=True
    ).exclude(id=service.id)[:5]

    context = {
        'title': service.name,
        'service': service,
        'similar_services': similar_services,
        'today': timezone.now().date(),
    }
    return render(request, 'services/detail.html', context)

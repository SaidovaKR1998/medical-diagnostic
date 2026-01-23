from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Service, ServiceCategory


def service_list(request):
    """Список всех услуг"""
    try:
        categories = ServiceCategory.objects.all()

        print(f"[DEBUG] Категорий: {categories.count()}")

        # Проверяем данные
        for cat in categories:
            print(f"[DEBUG] {cat.name}: {cat.services.count()} услуг")
            for service in cat.services.all()[:2]:
                print(f"  - {service.name}: {service.price} руб.")

        context = {
            'title': 'Наши услуги',
            'categories': categories,
        }

        # Используем простой шаблон для теста
        return render(request, 'services/list_simple.html', context)

    except Exception as e:
        print(f"[ERROR] service_list: {str(e)}")
        import traceback
        traceback.print_exc()

        # Возвращаем очень простую страницу с ошибкой
        return HttpResponse(f"""
        <h1>Ошибка загрузки услуг</h1>
        <p>Произошла ошибка: {str(e)}</p>
        <a href="/">На главную</a>
        """)

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

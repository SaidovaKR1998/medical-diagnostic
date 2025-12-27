from django.shortcuts import render

def home(request):
    """Главная страница"""
    context = {
        'title': 'Медицинская Диагностика - Главная',
        'services': [
            {'name': 'МРТ', 'icon': 'bi-magnet', 'description': 'Магнитно-резонансная томография'},
            {'name': 'КТ', 'icon': 'bi-cpu', 'description': 'Компьютерная томография'},
            {'name': 'УЗИ', 'icon': 'bi-soundwave', 'description': 'Ультразвуковая диагностика'},
            {'name': 'Анализы', 'icon': 'bi-droplet', 'description': 'Лабораторные исследования'},
        ]
    }
    return render(request, 'main/home.html', context)

def about(request):
    """Страница о компании"""
    return render(request, 'main/about.html', {'title': 'О компании'})

def contacts(request):
    """Страница контактов"""
    return render(request, 'main/contacts.html', {'title': 'Контакты'})

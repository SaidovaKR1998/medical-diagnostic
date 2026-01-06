# create_test_data.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from services.models import ServiceCategory, Service

print('Создаем категории услуг...')

# 1. Создаем категории
categories = [
    {'name': 'Аппаратная диагностика', 'icon': 'bi-magnet',
     'description': 'Современные аппаратные методы исследования'},
    {'name': 'Лабораторные исследования', 'icon': 'bi-droplet',
     'description': 'Анализы крови, мочи и другие лабораторные тесты'},
    {'name': 'Ультразвуковая диагностика', 'icon': 'bi-soundwave', 'description': 'УЗИ различных органов и систем'},
    {'name': 'Функциональная диагностика', 'icon': 'bi-activity',
     'description': 'ЭКГ, спирометрия и другие исследования'},
]

created_cats = []
for i, cat_data in enumerate(categories, 1):
    cat, created = ServiceCategory.objects.get_or_create(
        name=cat_data['name'],
        defaults={
            'icon': cat_data['icon'],
            'description': cat_data['description']
        }
    )
    created_cats.append(cat)
    print(f'{i}. {cat.name}')

print('\nСоздаем услуги...')

# 2. Создаем услуги
services_data = [
    # Аппаратная диагностика
    {'name': 'МРТ головного мозга', 'category': 0, 'price': 5200, 'duration': 60,
     'description': 'Магнитно-резонансная томография головного мозга'},
    {'name': 'КТ грудной клетки', 'category': 0, 'price': 4800, 'duration': 45,
     'description': 'Компьютерная томография органов грудной клетки'},
    {'name': 'Маммография', 'category': 0, 'price': 3500, 'duration': 30,
     'description': 'Рентгенологическое исследование молочных желез'},

    # Лабораторные исследования
    {'name': 'Общий анализ крови', 'category': 1, 'price': 850, 'duration': 15,
     'description': 'Развернутый клинический анализ крови'},
    {'name': 'Биохимический анализ крови', 'category': 1, 'price': 2200, 'duration': 20,
     'description': 'Комплексный биохимический анализ'},
    {'name': 'Анализ мочи общий', 'category': 1, 'price': 650, 'duration': 10,
     'description': 'Общий клинический анализ мочи'},

    # Ультразвуковая диагностика
    {'name': 'УЗИ брюшной полости', 'category': 2, 'price': 2700, 'duration': 40,
     'description': 'Ультразвуковое исследование органов брюшной полости'},
    {'name': 'УЗИ щитовидной железы', 'category': 2, 'price': 1900, 'duration': 30,
     'description': 'Ультразвуковое исследование щитовидной железы'},
    {'name': 'УЗИ молочных желез', 'category': 2, 'price': 2300, 'duration': 35,
     'description': 'Ультразвуковое исследование молочных желез'},

    # Функциональная диагностика
    {'name': 'ЭКГ (электрокардиограмма)', 'category': 3, 'price': 1200, 'duration': 20,
     'description': 'Электрокардиографическое исследование сердца'},
    {'name': 'Суточное мониторирование ЭКГ', 'category': 3, 'price': 4500, 'duration': 1440,
     'description': 'Холтеровское мониторирование сердечной деятельности'},
    {'name': 'Спирометрия', 'category': 3, 'price': 1800, 'duration': 30,
     'description': 'Исследование функции внешнего дыхания'},
]

for i, service_data in enumerate(services_data, 1):
    service, created = Service.objects.get_or_create(
        name=service_data['name'],
        defaults={
            'category': created_cats[service_data['category']],
            'price': service_data['price'],
            'duration': service_data['duration'],
            'description': service_data['description'],
            'full_description': f'Полное описание услуги "{service_data["name"]}". Современное оборудование, квалифицированные специалисты, точные результаты.',
            'preparation': 'Специальной подготовки не требуется' if service_data[
                                                                        'category'] != 1 else 'Сдача анализов проводится натощак',
            'contraindications': 'Индивидуальные противопоказания уточняйте у врача',
            'is_active': True
        }
    )
    print(f'{i}. {service.name} - {service.price} руб.')

print(f'\n✅ Готово! Создано:')
print(f'   - Категорий: {ServiceCategory.objects.count()}')
print(f'   - Услуг: {Service.objects.count()}')
print(f'   - Активных услуг: {Service.objects.filter(is_active=True).count()}')

# Добавляем создание врачей
print('\nСоздаем врачей...')

# Сначала создаем пользователей-врачей
doctors_data = [
    {
        'username': 'ivanov',
        'first_name': 'Иван',
        'last_name': 'Иванов',
        'email': 'ivanov@meddiagnostic.ru',
        'is_doctor': True,
        'specialty': 'Терапевт',
        'education': 'МГМУ им. Сеченова',
        'experience': 15,
    },
    {
        'username': 'petrova',
        'first_name': 'Мария',
        'last_name': 'Петрова',
        'email': 'petrova@meddiagnostic.ru',
        'is_doctor': True,
        'specialty': 'Кардиолог',
        'education': 'РНИМУ им. Пирогова',
        'experience': 12,
    },
    {
        'username': 'sidorov',
        'first_name': 'Алексей',
        'last_name': 'Сидоров',
        'email': 'sidorov@meddiagnostic.ru',
        'is_doctor': True,
        'specialty': 'Невролог',
        'education': 'СПбГМУ им. Павлова',
        'experience': 10,
    },
    {
        'username': 'smirnova',
        'first_name': 'Елена',
        'last_name': 'Смирнова',
        'email': 'smirnova@meddiagnostic.ru',
        'is_doctor': True,
        'specialty': 'УЗИ-специалист',
        'education': 'КГМУ',
        'experience': 8,
    },
]

for i, doc_data in enumerate(doctors_data, 1):
    # Создаем или получаем пользователя
    user, created = CustomUser.objects.get_or_create(
        username=doc_data['username'],
        defaults={
            'first_name': doc_data['first_name'],
            'last_name': doc_data['last_name'],
            'email': doc_data['email'],
            'is_doctor': True,
            'is_patient': False,
        }
    )

    if created:
        user.set_password('doctor123')  # Стандартный пароль
        user.save()

    # Создаем профиль врача
    doctor, doc_created = Doctor.objects.get_or_create(
        user=user,
        defaults={
            'specialty': doc_data['specialty'],
            'education': doc_data['education'],
            'experience': doc_data['experience'],
            'license_number': f'MED-LIC-{1000 + i}',
        }
    )

    if doc_created:
        print(f'{i}. Доктор {doc_data["first_name"]} {doc_data["last_name"]} - {doc_data["specialty"]}')
    else:
        print(f'{i}. Доктор {doc_data["first_name"]} {doc_data["last_name"]} уже существует')

print('\n✅ Всего создано:')
print(f'   - Врачей: {Doctor.objects.count()}')

from django.contrib import admin
from .models import Service, ServiceCategory

# Простая регистрация сначала
admin.site.register(ServiceCategory)
admin.site.register(Service)

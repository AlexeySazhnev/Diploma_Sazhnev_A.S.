from django.contrib import admin
from django.utils.html import format_html
from .models import Service, Record


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'image', 'show_photo']
    list_filter = ['name']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по названию услуги'
    list_editable = ['name', 'price', 'image']
    list_per_page = 10
    readonly_fields = ['show_photo']

    def show_photo(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="max-height:100px;">')
    show_photo.short_description = 'фото'


@admin.register(Record)
class AdminRecord(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_name', 'phone', 'date']
    list_filter = ['date']
    ordering = ['date']
    search_fields = ['last_name']
    search_help_text = 'Поиск по фамилии клиента'
    list_editable = ['date']
    list_per_page = 10
    fieldsets = [
        (
            'Клиент',
            {
                'fields': ['name', 'last_name', 'phone'],
                'classes': ['wide'],
            }
        ),
        (
            'Запись на услуги',
            {
                'fields': ['service', 'date'],
                'classes': ['wide'],
            },
        ),
    ]

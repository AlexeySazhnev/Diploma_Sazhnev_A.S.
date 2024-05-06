from django import forms
from .models import Service, Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
        widgets = {
            'service': forms.SelectMultiple(choices=[Service.objects.all()]),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
        }
        labels = {
            'name': 'Имя',
            'last_name': 'Фамилия',
            'phone': 'Телефон',
            'service': 'Услуга',
            'date': 'Дата и время для записи',
        }

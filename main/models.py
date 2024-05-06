from django.db import models

# Create your models here.Э


class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return f'{self.name} {self.price} {self.image}'


class Record(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    service = models.ManyToManyField(Service)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.name} {self.last_name} {self.phone} {self.service} {self.date}'

from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='logo/')
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


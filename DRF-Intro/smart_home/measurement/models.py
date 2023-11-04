from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name='Имя датчика')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, default='', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.sensor}'

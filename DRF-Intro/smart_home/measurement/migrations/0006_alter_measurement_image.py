# Generated by Django 4.2.3 on 2023-08-08 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_alter_measurement_options_alter_sensor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='Image/', verbose_name='Изображение'),
        ),
    ]
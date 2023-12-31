# Generated by Django 4.2.4 on 2023-08-19 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=30, verbose_name='Отчество')),
                ('organization_name', models.CharField(max_length=50, verbose_name='Название организации')),
                ('work_phone', models.DecimalField(decimal_places=0, max_digits=12, verbose_name='Рабочий телефон')),
                ('cell_phone', models.DecimalField(decimal_places=0, max_digits=12, verbose_name='Сотовый телефон')),
            ],
        ),
    ]

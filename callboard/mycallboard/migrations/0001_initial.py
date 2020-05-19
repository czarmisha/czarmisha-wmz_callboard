# Generated by Django 3.0.6 on 2020-05-17 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=7, verbose_name='Название типа')),
            ],
            options={
                'verbose_name': 'Тип объявления',
                'verbose_name_plural': 'Типы объявления',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Фото')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3, verbose_name='Название валюты')),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюты',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название района')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycallboard.City', verbose_name='Город района')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Объявление')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('phone', models.IntegerField(verbose_name='Номер телефона')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Платное')),
                ('is_moderation', models.BooleanField(default=False, verbose_name='Модерация')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('is_archive', models.BooleanField(default=False, verbose_name='Архивное')),
                ('ad_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycallboard.AdType', verbose_name='Тип объявления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycallboard.Category', verbose_name='Категория')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycallboard.City', verbose_name='Город')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycallboard.Currency', verbose_name='Валюта')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycallboard.District', verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]

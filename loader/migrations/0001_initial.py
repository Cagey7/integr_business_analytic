# Generated by Django 5.0.7 on 2024-08-05 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kato_name', models.CharField(max_length=512, verbose_name='КАТО название')),
                ('kato_code', models.CharField(max_length=16, verbose_name='КАТО коде')),
            ],
        ),
        migrations.CreateModel(
            name='Kfs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kfs_name', models.CharField(max_length=512, verbose_name='КФС название')),
                ('kfs_code', models.CharField(max_length=16, verbose_name='КФС код')),
            ],
        ),
        migrations.CreateModel(
            name='Krp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('krp_name', models.CharField(max_length=512, verbose_name='КРП название')),
                ('krp_code', models.CharField(max_length=16, verbose_name='КРП код')),
            ],
        ),
        migrations.CreateModel(
            name='Kse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kse_name', models.CharField(max_length=512, verbose_name='КСЕ название')),
                ('kse_code', models.CharField(max_length=16, verbose_name='КСЕ код')),
            ],
        ),
        migrations.CreateModel(
            name='Oked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oked_name', models.CharField(max_length=512, verbose_name='ОКЭД название')),
                ('oked_code', models.CharField(max_length=16, verbose_name='ОКЭД код')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=1024, verbose_name='Название организации на русском')),
                ('name_kz', models.CharField(max_length=1024, verbose_name='Название организации на казахском')),
                ('register_date', models.DateField(verbose_name='Время создания организации')),
                ('ceo', models.CharField(max_length=1024, verbose_name='Руководитель организации')),
                ('bin', models.CharField(max_length=12, verbose_name='БИН')),
                ('pay_nds', models.BooleanField(verbose_name='Плательщик НДС')),
                ('tax_risk', models.CharField(max_length=32, verbose_name='Степень риска налогоплательщика')),
                ('address_ru', models.CharField(max_length=1024, verbose_name='Адрес организации на русском')),
                ('address_kz', models.CharField(max_length=1024, verbose_name='Адрес организации на казахском')),
                ('phone_number', models.CharField(max_length=128, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=512, verbose_name='Электронная почта')),
                ('kato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loader.kato', verbose_name='КАТО')),
                ('kfs', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loader.kfs', verbose_name='КФС')),
                ('krp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loader.krp', verbose_name='КРП')),
                ('kse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loader.kse', verbose_name='КСЕ')),
                ('primary_oked', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='primary_oked', to='loader.oked', verbose_name='ОКЭД')),
                ('secondary_okeds', models.ManyToManyField(related_name='secondary_okeds', to='loader.oked')),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-08-26 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loader', '0009_alter_company_address_kz_alter_company_address_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxes',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='taxes', to='loader.company', verbose_name='Организация'),
        ),
    ]

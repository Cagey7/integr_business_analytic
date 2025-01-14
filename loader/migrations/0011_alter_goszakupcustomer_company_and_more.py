# Generated by Django 5.0.2 on 2024-08-26 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loader', '0010_alter_taxes_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goszakupcustomer',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='goszakupcustomer', to='loader.company', verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='goszakupsupplier',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='goszakupsupplier', to='loader.company', verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='nds',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='nds', to='loader.company', verbose_name='Организация'),
        ),
    ]

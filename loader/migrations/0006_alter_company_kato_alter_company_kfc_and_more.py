# Generated by Django 5.0.7 on 2024-08-06 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loader', '0005_rename_kfс_company_kfc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='kato',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='loader.kato', verbose_name='КАТО'),
        ),
        migrations.AlterField(
            model_name='company',
            name='kfc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='loader.kfc', verbose_name='КФС'),
        ),
        migrations.AlterField(
            model_name='company',
            name='krp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='loader.krp', verbose_name='КРП'),
        ),
        migrations.AlterField(
            model_name='company',
            name='kse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='loader.kse', verbose_name='КСЕ'),
        ),
        migrations.AlterField(
            model_name='company',
            name='primary_oked',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='primary_oked', to='loader.oked', verbose_name='ОКЭД'),
        ),
    ]

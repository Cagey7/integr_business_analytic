# Generated by Django 5.0.7 on 2024-08-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loader', '0007_alter_company_pay_nds_alter_company_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='tax_risk',
            field=models.CharField(max_length=32, null=True, verbose_name='Степень риска налогоплательщика'),
        ),
    ]
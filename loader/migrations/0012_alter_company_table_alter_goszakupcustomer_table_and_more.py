# Generated by Django 5.0.7 on 2024-08-29 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loader', '0011_alter_goszakupcustomer_company_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='company',
            table='companies',
        ),
        migrations.AlterModelTable(
            name='goszakupcustomer',
            table='gos_zakup_customer',
        ),
        migrations.AlterModelTable(
            name='goszakupsupplier',
            table='gos_zakup_supplier',
        ),
        migrations.AlterModelTable(
            name='kato',
            table='kato',
        ),
        migrations.AlterModelTable(
            name='kfc',
            table='kfc',
        ),
        migrations.AlterModelTable(
            name='krp',
            table='krp',
        ),
        migrations.AlterModelTable(
            name='kse',
            table='kse',
        ),
        migrations.AlterModelTable(
            name='nds',
            table='nds',
        ),
        migrations.AlterModelTable(
            name='oked',
            table='oked',
        ),
        migrations.AlterModelTable(
            name='taxes',
            table='taxes',
        ),
    ]
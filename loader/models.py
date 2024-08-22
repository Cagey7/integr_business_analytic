from django.db import models


class Company(models.Model):
    name_ru = models.CharField(max_length=1024, null=True, verbose_name="Название организации на русском")
    name_kz = models.CharField(max_length=1024, null=True, verbose_name="Название организации на казахском")
    register_date = models.DateField(null=True, verbose_name="Время создания организации")
    ceo = models.CharField(max_length=1024, null=True, verbose_name="Руководитель организации")
    company_bin = models.CharField(max_length=12, unique=True, verbose_name="БИН")
    pay_nds = models.BooleanField(null=True, verbose_name="Плательщик НДС")
    tax_risk = models.CharField(max_length=32, null=True, verbose_name="Степень риска налогоплательщика")
    address_ru = models.CharField(max_length=1024, null=True, verbose_name="Адрес организации на русском")
    address_kz = models.CharField(max_length=1024, null=True, verbose_name="Адрес организации на казахском")
    phone_number = models.CharField(max_length=128, null=True, verbose_name="Номер телефона")
    email = models.CharField(max_length=254, null=True, verbose_name="Электронная почта")
    krp = models.ForeignKey("Krp", on_delete=models.PROTECT, null=True, verbose_name="КРП")
    kse = models.ForeignKey("Kse", on_delete=models.PROTECT, null=True, verbose_name="КСЕ")
    kfc = models.ForeignKey("Kfc", on_delete=models.PROTECT, null=True, verbose_name="КФС")
    kato = models.ForeignKey("Kato", on_delete=models.PROTECT, null=True, verbose_name="КАТО")
    primary_oked = models.ForeignKey("Oked", on_delete=models.PROTECT, null=True, related_name="primary_oked", verbose_name="ОКЭД")
    secondary_okeds = models.ManyToManyField("Oked", related_name="secondary_okeds")
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name_ru}"


class Krp(models.Model):
    krp_code = models.IntegerField(unique=True, verbose_name="КРП код")
    krp_name = models.CharField(max_length=512, verbose_name="КРП название")
    
    
    def __str__(self):
        return f"{self.krp_name}"
    
class Kse(models.Model):
    kse_code = models.IntegerField(unique=True, verbose_name="КСЕ код")
    kse_name = models.CharField(max_length=512, verbose_name="КСЕ название")


    def __str__(self):
        return f"{self.kse_name}"


class Kfc(models.Model):
    kfc_code = models.IntegerField(unique=True, verbose_name="КФС код")
    kfc_name = models.CharField(max_length=512, verbose_name="КФС название")


    def __str__(self):
        return f"{self.kfc_name}"


class Kato(models.Model):
    kato_code = models.IntegerField(unique=True, verbose_name="КАТО коде")
    kato_name = models.CharField(max_length=512, verbose_name="КАТО название")
    

    def __str__(self):
        return f"{self.kato_name}"


class Oked(models.Model):
    oked_code = models.IntegerField(unique=True, verbose_name="ОКЭД код")
    oked_name = models.CharField(max_length=512, verbose_name="ОКЭД название")


    def __str__(self):
        return f"{self.oked_name}"


class Taxes(models.Model):
    year = models.IntegerField(verbose_name="Год")
    value = models.FloatField(verbose_name="Значение")
    company = models.ForeignKey("Company", on_delete=models.PROTECT, verbose_name="Организация")


class Nds(models.Model):
    year = models.IntegerField(verbose_name="Год")
    value = models.FloatField(verbose_name="Значение")
    company = models.ForeignKey("Company", on_delete=models.PROTECT, verbose_name="Организация")


class GosZakupSupplier(models.Model):
    year = models.IntegerField(verbose_name="Год")
    value = models.FloatField(verbose_name="Значение")
    company = models.ForeignKey("Company", on_delete=models.PROTECT, verbose_name="Организация")


class GosZakupCustomer(models.Model):
    year = models.IntegerField(verbose_name="Год")
    value = models.FloatField(verbose_name="Значение")
    company = models.ForeignKey("Company", on_delete=models.PROTECT, verbose_name="Организация")


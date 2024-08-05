from django.db import models


class Company(models.Model):
    name_ru = models.CharField(max_length=1024, verbose_name="Название организации на русском")
    name_kz = models.CharField(max_length=1024, verbose_name="Название организации на казахском")
    register_date = models.DateField(verbose_name="Время создания организации")
    ceo = models.CharField(max_length=1024, verbose_name="Руководитель организации")
    bin = models.CharField(max_length=12, verbose_name="БИН")
    pay_nds = models.BooleanField(verbose_name="Плательщик НДС")
    tax_risk = models.CharField(max_length=32, verbose_name="Степень риска налогоплательщика")
    address_ru = models.CharField(max_length=1024, verbose_name="Адрес организации на русском")
    address_kz = models.CharField(max_length=1024, verbose_name="Адрес организации на казахском")
    phone_number = models.CharField(max_length=128, verbose_name="Номер телефона")
    email = models.CharField(max_length=512, verbose_name="Электронная почта")
    krp = models.ForeignKey("Krp", on_delete=models.PROTECT, verbose_name="КРП")
    kse = models.ForeignKey("Kse", on_delete=models.PROTECT, verbose_name="КСЕ")
    kfs = models.ForeignKey("Kfs", on_delete=models.PROTECT, verbose_name="КФС")
    kato = models.ForeignKey("Kato", on_delete=models.PROTECT, verbose_name="КАТО")
    primary_oked = models.ForeignKey("Oked", on_delete=models.PROTECT, related_name="primary_oked", verbose_name="ОКЭД")
    secondary_okeds = models.ManyToManyField("Oked", related_name="secondary_okeds")
    
    def __str__(self):
        return f"{self.name_ru}"


class Krp(models.Model):
    krp_name = models.CharField(max_length=512, verbose_name="КРП название")
    krp_code = models.CharField(max_length=16, verbose_name="КРП код")
    
    
    def __str__(self):
        return f"{self.krp_name}"
    
class Kse(models.Model):
    kse_name = models.CharField(max_length=512, verbose_name="КСЕ название")
    kse_code = models.CharField(max_length=16, verbose_name="КСЕ код")


    def __str__(self):
        return f"{self.kse_name}"


class Kfs(models.Model):
    kfs_name = models.CharField(max_length=512, verbose_name="КФС название")
    kfs_code = models.CharField(max_length=16, verbose_name="КФС код")


    def __str__(self):
        return f"{self.kfs_name}"


class Kato(models.Model):
    kato_name = models.CharField(max_length=512, verbose_name="КАТО название")
    kato_code = models.CharField(max_length=16, verbose_name="КАТО коде")


    def __str__(self):
        return f"{self.kato_name}"


class Oked(models.Model):
    oked_name = models.CharField(max_length=512, verbose_name="ОКЭД название")
    oked_code = models.CharField(max_length=16, verbose_name="ОКЭД код")


    def __str__(self):
        return f"{self.oked_name}"
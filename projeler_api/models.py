from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Personel(models.Model):
    personel_adi=models.CharField(max_length=50)

    def __str__(self):
        return self.personel_adi


class Project(models.Model):
    COUNTRIES = (('TURKIYE', 'Türkiye'), ('GERMANY', 'Almanya'), ('FRANCE', 'Fransa'))
    ulke = models.CharField(max_length=50, name="Ülke", choices=COUNTRIES, null=True, blank=True)

    bolge = models.CharField(max_length=50, blank=True, null=True)
    firma = models.CharField(max_length=200, blank=True, null=True)
    proje_adi = models.CharField(max_length=200, blank=True, null=True)
    proje_turu = models.CharField(max_length=50, blank=True, null=True)
    kod = models.CharField(max_length=4, blank=True, null=True)
    proje_suresi = models.CharField(max_length=10, blank=True, null=True)
    adres = models.TextField(blank=True, null=True)
    telefon = models.CharField(max_length=15, blank=True, null=True)
    faks = models.CharField(max_length=15, blank=True, null=True)
    genel_mudur = models.CharField(max_length=50, blank=True, null=True, verbose_name="Genel Müdür", )
    proje_direktoru = models.CharField(max_length=50, blank=True, null=True)
    proje_muduru = models.CharField(max_length=50, blank=True, null=True)
    proje_mudur_yrd = models.CharField(max_length=50, blank=True, null=True)
    santiye_sefi = models.CharField(max_length=50, blank=True, null=True)
    teknik_ofis_muduru = models.CharField(max_length=50, blank=True, null=True)
    teknik_ofis_elemani = models.CharField(max_length=50, blank=True, null=True)
    dizayn_ofis_sefi = models.CharField(max_length=50, blank=True, null=True)
    planlama_sefi = models.CharField(max_length=50, blank=True, null=True)
    butce_kontrol_muduru = models.CharField(max_length=50, blank=True, null=True)
    ince_isler_sefi = models.CharField(max_length=50, blank=True, null=True)
    elektromekanik_muduru = models.CharField(max_length=50, blank=True, null=True)
    mekanik_isler_sefi = models.CharField(max_length=50, blank=True, null=True)
    elektrik_isler_sefi = models.CharField(max_length=50, blank=True, null=True)
    idari_isler_sefi = models.CharField(max_length=50, blank=True, null=True)
    altyapi_isler_sefi = models.CharField(max_length=50, blank=True, null=True)
    ihale_ve_sozlesme_uzmani = models.CharField(max_length=50, blank=True, null=True)
    maliyet_kontrol_sorumlusu = models.CharField(max_length=50, blank=True, null=True)
    kalite_kontrol_muhendisi = models.CharField(max_length=50, blank=True, null=True)
    finans_muduru = models.CharField(max_length=50, blank=True, null=True)
    muhasebe_muduru = models.CharField(max_length=50, blank=True, null=True)
    muhasebe_sorumlusu = models.CharField(max_length=50, blank=True, null=True)
    insan_kaynaklari = models.CharField(max_length=50, blank=True, null=True)
    satinalma_genel_muduru = models.CharField(max_length=50, blank=True, null=True)
    satinalma_muduru = models.CharField(max_length=50, blank=True, null=True)
    merkez_satinalma_sorumlusu1 = models.CharField(max_length=50, blank=True, null=True)
    merkez_satinalma_sorumlusu2 = models.CharField(max_length=50, blank=True, null=True)
    santiye_satinalma_sorumlusu1 = models.CharField(max_length=50, blank=True, null=True)
    santiye_satinalma_sorumlusu2 = models.CharField(max_length=50, blank=True, null=True)
    depo_sorumlusu = models.CharField(max_length=50, blank=True, null=True)
    depo_elemani = models.CharField(max_length=50, blank=True, null=True)
    proje_personeli = models.ManyToManyField(Personel,null=True)


    def __str__(self):
        return self.kod
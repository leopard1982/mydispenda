from django.db import models
from django.contrib.auth.models import User

# Create your models here.
kelamin = [
    ('P','Pria'),
    ('W','Wanita')
]

class Jabatan(models.Model):
    Kode = models.CharField(max_length=3,primary_key=True,null=False,blank=False,default='',verbose_name='Kode Jabatan')
    Nama_Jabatan = models.CharField(max_length=20,verbose_name='Nama Jabatan')

    def __str__ (self):
        return self.Nama_Jabatan
    
class Struktur(models.Model):
    Kode = models.CharField(max_length=3,primary_key=True,null=False,blank=False,default='',verbose_name='Kode Jabatan')
    Nama_Struktur = models.CharField(max_length=20,verbose_name='Nama Struktur')

    def __str__ (self):
        return self.Nama_Struktur

class Pegawai(models.Model):
    NIP = models.CharField(max_length=20,primary_key=True,default='',null=False,blank=False,verbose_name='Nomor Induk Pegawai*')
    Jabatan = models.ForeignKey(Jabatan,verbose_name='Jabatan*',null=False,blank=False,on_delete=models.RESTRICT)
    Struktur = models.ForeignKey(Struktur,verbose_name='Struktur*',null=False,blank=False,on_delete=models.RESTRICT)
    Nama = models.CharField(max_length=50, verbose_name='Nama Pegawai*')
    Kelamin = models.CharField(max_length=1,choices=kelamin,verbose_name='Jenis Kelamin*')

    def __str__(self):
        return self.Nama

class Konfigurasi(models.Model):
    Kepala_Bapeda = models.OneToOneField(Pegawai,on_delete=models.RESTRICT)
    isPLT = models.BooleanField(default=False)


class RealUser(User):
    isCreate = models.BooleanField(default=False)
    isUpdate = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)

class DasarSuratTugas(models.Model):
    dasar = models.CharField(max_length=200,primary_key=True,default="")

class SuratTugas(models.Model):
    Nomor_Surat = models.CharField(max_length=20,default='',primary_key=True,blank=False,null=False)
    Tanggal_Surat = models.DateField(auto_now_add=False)
    Tugas = models.CharField(max_length=200)
    Lokasi_Tugas = models.CharField(max_length=30)
    Tanggal_Tugas = models.CharField(max_length=30)
    Kepala_Bapeda = models.CharField(max_length=50,null=True,blank=True)
    Ketua_Tim = models.ForeignKey(Pegawai,on_delete=models.RESTRICT)
    isDone = models.BooleanField(default=False)

class ST_Dasar(models.Model):
    Nomor_Surat = models.ForeignKey(SuratTugas, on_delete=models.RESTRICT)
    Dasar = models.ForeignKey(DasarSuratTugas,on_delete=models.RESTRICT)

    class Meta:
        unique_together = ['Nomor_Surat','Dasar']

class ST_Peserta(models.Model):
    Nomor_Surat = models.ForeignKey(SuratTugas,on_delete=models.RESTRICT)
    Peserta = models.ForeignKey(Pegawai,on_delete=models.RESTRICT)

    class Meta:
        unique_together = ['Nomor_Surat','Peserta']




from django import forms
from surat.models import Pegawai, Jabatan, Struktur, Konfigurasi, SuratTugas, RealUser
from django.contrib.auth.models import User

class Konfigurasi_Form(forms.Form):
    class Meta:
        model = Konfigurasi
        fields = "__all__"

class SuratTugas_Form(forms.ModelForm):
    class Meta:
        model = SuratTugas
        fields = "__all__"

        widgets = {
            'Nomor_Surat': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Nomor Surat'}),
            'Tanggal_Surat': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'misal. 14 - 16 Maret 2023'}),
            'Tugas': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Detail Penugasan'}),
            'Lokasi_Tugas': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Lokasi Tugas'}),
            'Tanggal_Tugas': forms.DateInput(attrs={'class':'form-control my-1','required':'required'}),    
            'Kepala_Bapeda': forms.Select(attrs={'class':'form-select my-1','required':'required'}),        
        }

class SuratTugas_Update(forms.ModelForm):
    class Meta:
        model = SuratTugas
        fields = "__all__"

        widgets = {
            'Nomor_Surat': forms.TextInput(attrs={'class':'form-control my-1','required':'required','readonly':'readonly','placeholder':'Nomor Surat'}),
            'Tanggal_Surat': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'misal. 14 - 16 Maret 2023'}),
            'Tugas': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Detail Penugasan'}),
            'Lokasi_Tugas': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Lokasi Tugas'}),
            'Tanggal_Tugas': forms.DateInput(attrs={'class':'form-control my-1','required':'required'}),    
            'Kepala_Bapeda': forms.Select(attrs={'class':'form-select my-1','required':'required'}),        
        }


class Jabatan_Form(forms.ModelForm):
    class Meta:
        model = Jabatan
        fields = "__all__"

        widgets = {
            'Kode': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Kode Jabatan'}),
            'Nama_Jabatan': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Nama Jabatan'}),
        }

class Jabatan_Update(forms.ModelForm):
    class Meta:
        model = Jabatan
        fields = "__all__"

        widgets = {
            'Kode': forms.TextInput(attrs={'class':'form-control my-1','required':'required','readonly':'readonly','placeholder':'Kode Jabatan'}),
            'Nama_Jabatan': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Nama Jabatan'}),
        }

class Struktur_Form(forms.ModelForm):
    class Meta:
        model = Struktur
        fields = "__all__"

        widgets = {
            'Kode': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Kode Stuktur Jabatan'}),
            'Nama_Struktur': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Nama Struktur Jabatan'}),
        }

class Struktur_Update(forms.ModelForm):
    class Meta:
        model = Struktur
        fields = "__all__"

        widgets = {
            'Kode': forms.TextInput(attrs={'class':'form-control my-1','required':'required','readonly':'readonly','placeholder':'Kode Jabatan'}),
            'Nama_Struktur': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Nama Jabatan'}),
        }

class Pegawai_Form(forms.ModelForm):
    class Meta:
        model = Pegawai
        fields = "__all__"

        widgets = {
            'NIP': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Masukkan NIP Pegawai'}),
            'Jabatan': forms.Select(attrs={'class':'form-select my-1','required':'required'}),
            'Struktur': forms.Select(attrs={'class':'form-select my-1','required':'required'}),
            'Nama': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Masukkan Nama Pegawai'}),
            'Kelamin': forms.Select(attrs={'class':'form-select my-1','required':'required'}),
        }

class Pegawai_Update(forms.ModelForm):
    class Meta:
        model = Pegawai
        fields = "__all__"

        widgets = {
            'NIP': forms.TextInput(attrs={'class':'form-control my-1','required':'required','readonly':'readonly','placeholder':'Masukkan NIP Pegawai'}),
            'Jabatan': forms.Select(attrs={'class':'form-select my-1','required':'required'}),
            'Struktur': forms.Select(attrs={'class':'form-select my-1','required':'required'}),
            'Nama': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Masukkan Nama Pegawai'}),
            'Kelamin': forms.Select(attrs={'class':'form-select my-1','required':'required'}),
        }

class SuratTugas_Form(forms.ModelForm):
    class Meta:
        model = SuratTugas
        fields = "__all__"

        widgets = {
            'Nomor_Surat': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Nomor Surat'}),
            'Tanggal_Surat': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'misal. 14 - 16 Maret 2023'}),
            'Tugas': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Detail Penugasan'}),
            'Lokasi_Tugas': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Lokasi Tugas'}),
            'Tanggal_Tugas': forms.DateInput(attrs={'class':'form-control my-1','required':'required'}),    
            'Kepala_Bapeda': forms.Select(attrs={'class':'form-select my-1','required':'required'}),        
        }

class SuratTugas_Update(forms.ModelForm):
    class Meta:
        model = SuratTugas
        fields = "__all__"

        widgets = {
            'Nomor_Surat': forms.TextInput(attrs={'class':'form-control my-1','required':'required','readonly':'readonly','placeholder':'Nomor Surat'}),
            'Tanggal_Surat': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'misal. 14 - 16 Maret 2023'}),
            'Tugas': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Detail Penugasan'}),
            'Lokasi_Tugas': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Lokasi Tugas'}),
            'Tanggal_Tugas': forms.DateInput(attrs={'class':'form-control my-1','required':'required'}),    
            'Kepala_Bapeda': forms.Select(attrs={'class':'form-select my-1','required':'required'}),        
        }

class User_Form(forms.ModelForm):
    class Meta:
        model = RealUser
        fields = ['username','password','isCreate','isUpdate']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Username'}),
            'password': forms.TextInput(attrs={'type':'password','class':'form-control my-1','required':'required','placeholder':'Password'}),
            'isCreate': forms.CheckboxInput(attrs={'class':'form-check-input my-1'}),
            'isUpdate': forms.CheckboxInput(attrs={'class':'form-check-input my-1'}),        
        }

class User_Update(forms.ModelForm):
    class Meta:
        model = RealUser
        fields = ['username','password','isCreate','isUpdate']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Username','readonly':'readonly'}),
            'password': forms.TextInput(attrs={'type':'password','class':'form-control my-1','required':'required','placeholder':'Password'}),
            'isCreate': forms.CheckboxInput(attrs={'class':'form-check-input my-1'}),
            'isUpdate': forms.CheckboxInput(attrs={'class':'form-check-input my-1'}),        
        }


class Konfigurasi_Form(forms.ModelForm):
    class Meta:
        model = Konfigurasi
        fields = ['Kepala_Bapeda','isPLT']

        widgets = {
            'Kepala_Bapeda': forms.Select(attrs={'class':'form-select my-1','required':'required'}),
            'isPLT': forms.CheckboxInput(attrs={'class':'form-check-input my-1'}),        
        }

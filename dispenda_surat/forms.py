from django import forms
from dispenda_surat.models import Pegawai, Jabatan, Struktur, Konfigurasi, SuratTugas,  DasarSuratTugas, LaporanEval
# from django.contrib.auth.models import User
from dispenda_surat.models import ExtendUser
from bootstrap_datepicker_plus.widgets import DatePickerInput

class Konfigurasi_Form(forms.Form):
    class Meta:
        model = Konfigurasi
        fields = "__all__"

class SuratTugas_Form(forms.ModelForm):
    class Meta:
        model = SuratTugas
        fields = ['Nomor_Surat','Tanggal_Surat','Ketua_Tim','Tugas','Lokasi_Tugas','Tanggal_Tugas']

        widgets = {
            'Nomor_Surat': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Nomor Surat'}),
            'Tanggal_Surat': DatePickerInput(attrs={'class':'form-control my-1','required':'required'}),
            'Ketua_Tim': forms.Select(attrs={'class':'form-select my-1','required':'required'}),
            'Tugas': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Detail Penugasan'}),
            'Lokasi_Tugas': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Lokasi Tugas'}),
            'Tanggal_Tugas': forms.DateInput(attrs={'class':'form-control my-1','required':'required','placeholder': 'misal: 17-21 Maret 2023'}),    
        }

class SuratTugas_Update(forms.ModelForm):
    class Meta:
        model = SuratTugas
        fields = ['Nomor_Surat','Tanggal_Surat','Tugas','Lokasi_Tugas','Tanggal_Tugas']

        widgets = {
            'Nomor_Surat': forms.TextInput(attrs={'class':'form-control my-1','required':'required','readonly':'readonly','placeholder':'Nomor Surat'}),
            'Tanggal_Surat': DatePickerInput(),
            'Tugas': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Detail Penugasan'}),
            'Lokasi_Tugas': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Lokasi Tugas'}),
            'Tanggal_Tugas': forms.TextInput(attrs={'class':'form-control my-1','required':'required'}),         
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



class User_Form(forms.ModelForm):
    class Meta:
        model = ExtendUser
        fields = ['username','password']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Username'}),
            'password': forms.TextInput(attrs={'type':'password','class':'form-control my-1','required':'required','placeholder':'Password'}),
            # 'isCreate': forms.CheckboxInput(attrs={'class':'form-check-input my-1'}),
            # 'isUpdate': forms.CheckboxInput(attrs={'class':'form-check-input my-1'}),        
        }

class User_Update(forms.ModelForm):
    class Meta:
        model = ExtendUser
        fields = ['username','password']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Username','readonly':'readonly'}),
            'password': forms.TextInput(attrs={'type':'password','class':'form-control my-1','required':'required','placeholder':'Password'}),
                  
        }


class Konfigurasi_Form(forms.ModelForm):
    class Meta:
        model = Konfigurasi
        fields = ['Kepala_Bapeda','isPLT']

        widgets = {
            'Kepala_Bapeda': forms.Select(attrs={'class':'form-select my-1','required':'required'}),
            'isPLT': forms.CheckboxInput(attrs={'class':'form-check-input my-1'}),        
        }

class DasarSuratTugas_Form(forms.ModelForm):
    class Meta:
        model = DasarSuratTugas
        fields = ['dasar']

        widgets = {
            'dasar': forms.TextInput(attrs={'class':'form-control my-1','required':'required'}),        
        }

class Evaluasi_Form(forms.ModelForm):
    class Meta:
        model = LaporanEval
        fields = "__all__"
        exclude = ['isDone']

        widgets = {
            'Nomor_Surat_Tugas': forms.Select(attrs={'class':'form-select my-1','required':'required'}),
            'Nomor_Surat_Eval': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Nomor Surat Evaluasi'}),
            'Tanggal_Surat_Eval': DatePickerInput(attrs={'class':'form-control my-1','required':'required'}),
            'Tahun_Anggaran': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'misal. 2024'}),
            'Periode_Awal': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'misal. Januari 2023'}),
            'Periode_Akhir': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'misal. Desember 2023'}),
            'Periode_Pegawai': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'misal. Desember 2023'}),
            'UPPD': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'diisi nama UPPD'}),    
        }
    
    def __init__(self, *args, **kwargs):
        super(Evaluasi_Form,self).__init__(*args, **kwargs)
        self.fields['Nomor_Surat_Tugas'].queryset = SuratTugas.objects.all().filter(isDone=True)

class Evaluasi_Form_Update(forms.ModelForm):
    class Meta:
        model = LaporanEval
        fields = "__all__"
        exclude = ['isDone']

        widgets = {
            'Nomor_Surat_Tugas': forms.Select(attrs={'class':'form-select my-1','required':'required','disabled':'disabled'}),
            'Nomor_Surat_Eval': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'Nomor Surat Evaluasi','readonly':'readonly'}),
            'Tanggal_Surat_Eval': DatePickerInput(attrs={'class':'form-control my-1','required':'required','readonly':'readonly'}),
            'Tahun_Anggaran': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'misal. 2024'}),
            'Periode_Awal': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'misal. Januari 2023'}),
            'Periode_Akhir': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'misal. Desember 2023'}),
            'Periode_Pegawai': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'misal. Desember 2023'}),
            'UPPD': forms.TextInput(attrs={'class':'form-control my-1','required':'required','placeholder':'diisi nama UPPD'}),    
        }
    
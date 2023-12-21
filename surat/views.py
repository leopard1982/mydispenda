from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from surat.forms import Pegawai_Form, Jabatan_Form, SuratTugas_Form,Pegawai_Update, Struktur_Form
from surat.forms import SuratTugas_Update, Struktur_Update, User_Form, Konfigurasi_Form, SuratTugas_Form
from surat.forms import DasarSuratTugas_Form
from surat.models import Pegawai,Jabatan, Struktur, RealUser, Konfigurasi, SuratTugas,DasarSuratTugas
from surat.models import ST_Dasar, ST_Peserta
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.conf import settings
import os
import random
import docx

# Create your views here.
def Login(request):
    print('login')
    if(request.user.is_authenticated):
        print('belum login')
        return render(request,'dashboard.html')
    else:
        print('lagi mau login')
        if request.method == "POST":
            print('ini submit')
            x='human' in request.POST
            if x:
                print('ini adalah manusia')
                username=request.POST['username']
                password=request.POST['password']
                user = authenticate(username=username,password=password)
                if(user is not None):
                    print('login berhasil')
                    login(request,user)
                    return HttpResponseRedirect('/')
        return render(request,'login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def Pegawai_create(request):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        myform = Pegawai_Form(request.POST)
        if myform.is_valid():
            myform.save()
    
    myform = Pegawai_Form()
    context = {
        'myform': myform,
    }
    return render(request,'pegawai/create.html', context)

def Pegawai_update(request):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/')
    myform = SuratTugas_Form()
    print("test")
    return render(request,'pegawai/update.html',{'myform':myform})

def Pegawai_list(request):
    if(not request.user.is_authenticated):
        return HttpResponseRedirect('/')
    data = Pegawai.objects.all()
    context = {
        'data':data
    }
    return render(request,'pegawai/list.html',context)

def Pegawai_delete(request):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/pegawai/list/')

def Jabatan_create(request):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        myform = Jabatan_Form(request.POST)
        if myform.is_valid():
            myform.save()
    
    myform = Jabatan_Form()
    context = {
        'myform': myform
    }
    return render(request,'jabatan/create.html', context)

def Jabatan_update(request):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/')
    return render(request,'jabatan/update.html')

def Jabatan_list(request):
    if(not request.user.is_authenticated):
        return HttpResponseRedirect('/')
    data = Jabatan.objects.all()
    context = {
        'data':data
    }
    return render(request,'jabatan/list.html',context)

def Jabatan_delete(request):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/jabatan/list/')

def Struktur_create(request):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        myform = Struktur_Form(request.POST)
        if myform.is_valid():
            myform.save()
    
    myform = Struktur_Form()
    context = {
        'myform': myform
    }
    return render(request,'struktur/create.html', context)

def Struktur_update(request):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/')
    
    return render(request,'struktur/update.html')

def Struktur_list(request):
    if(not request.user.is_authenticated):
        return HttpResponseRedirect('/')
    data = Struktur.objects.all()
    context = {
        'data':data
    }
    return render(request,'struktur/list.html',context)

def Struktur_delete(request):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/struktur/list/')


def User_create(request):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        myform = User_Form(request.POST)
        if myform.is_valid():
            myform.save()
            user = RealUser.objects.get(username=request.POST.get('username'))
            user.set_password(request.POST.get('password'))
            user.save()
        else:
            print(myform)
    
    myform = User_Form()
    context = {
        'myform': myform
    }
    return render(request,'user/create.html', context)

def User_update(request):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/')
    
    return render(request,'struktur/update.html')

def User_list(request):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/')
    data = RealUser.objects.all()
    context = {
        'data':data
    }
    return render(request,'user/list.html',context)

def User_delete(request):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/struktur/list/')

def Konfigurasi_create(request):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/')
    if(Konfigurasi.objects.all().count()>0):
        return HttpResponseRedirect('/konfigurasi/list/')
    if request.method == 'POST':
        myform = Konfigurasi_Form(request.POST)
        if myform.is_valid():
            myform.save()
            return HttpResponseRedirect('/konfigurasi/list/')
    
    myform = Konfigurasi_Form()
    context = {
        'myform': myform
    }
    return render(request,'konfigurasi/create.html', context)

def Konfigurasi_list(request):
    if(not request.user.is_superuser):
        return HttpResponseRedirect('/')
    if(Konfigurasi.objects.all().count()==0):
        return HttpResponseRedirect('/konfigurasi/create/')
    
    data = Konfigurasi.objects.all()[0]
    context = {
        'data': data
    }
    return render(request,'konfigurasi/list.html', context)

def SuratTugas_create(request):
    if(not request.user.is_authenticated):
        return HttpResponseRedirect('/')
    
    isGet = False
    try:
        nomorsurat = request.GET['surat']
        isGet=True
    except:
        pass

    if(isGet):
        surattugas = SuratTugas.objects.all().get(Nomor_Surat=nomorsurat)
        
        peserta = ST_Peserta.objects.filter(Nomor_Surat=surattugas)
        dasar = ST_Dasar.objects.filter(Nomor_Surat=surattugas)
        

        list_peserta = Pegawai.objects.all().filter(~Q(Nama=surattugas.Ketua_Tim) & ~Q(Nama=surattugas.Kepala_Bapeda))
        list_dasar = DasarSuratTugas.objects.all()
        
        context = {
                'surattugas':surattugas,
                'peserta': peserta,
                'dasar':dasar,
                'list_peserta':list_peserta,
                'list_dasar':list_dasar,
        }
        return render(request,'surattugas/create_detail.html',context)
    
    if(request.method == 'POST'):
        form = SuratTugas_Form(request.POST)
        if(form.is_valid()):
            form.save()
            Kepala_Bapedanya = Konfigurasi.objects.all()[0].Kepala_Bapeda.Nama
            SuratTugas.objects.filter(Nomor_Surat = request.POST['Nomor_Surat']).update(Kepala_Bapeda=Kepala_Bapedanya, ID_NomorSurat=random.random()*1000000)
            return HttpResponseRedirect('/surattugas/create/?surat=' + request.POST['Nomor_Surat'])
    form = SuratTugas_Form()
    context = {
        'form':form
    }
    return render(request,'surattugas/create.html', context)

def SuratTugas_list(request):
    data = SuratTugas.objects.all()
    context = {
        'data':data
    }
    return render(request,'surattugas/list.html', context)

def DasarTugas_create(request):
    if(not request.user.is_authenticated):
        return HttpResponseRedirect('/')
    if(request.method == 'POST'):
        form = DasarSuratTugas_Form(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/dasartugas/list/')
    form = DasarSuratTugas_Form()
    context = {
        'form':form
    }
    return render(request,'dasarnya/create.html', context)

def DasarTugas_list(request):
    data = DasarSuratTugas.objects.all()
    context = {
        'data':data
    }
    return render(request,'dasarnya/list.html', context)

def Anggota_Tambah(request):
    try:
        nomorsurat = request.GET['surat']
    except:
        return HttpResponseRedirect('/surattugas/list/')
    try:
        st_peserta = ST_Peserta()
        #.objects.create(Dasar=DasarSuratTugas.objects.get(dasar=request.POST['dasarnya']),Surat_Tugas=SuratTugas.objects.get(Nomor_Surat=nomorsurat))
        st_peserta.Nomor_Surat = SuratTugas.objects.get(Nomor_Surat=nomorsurat)
        st_peserta.Peserta = Pegawai.objects.get(NIP=request.POST['pesertanya'])
        st_peserta.save()
    except:
        pass
    return HttpResponseRedirect('/surattugas/create/?surat=' + nomorsurat)

def Dasar_Tambah(request):
    try:
        nomorsurat = request.GET['surat']
    except:
        return HttpResponseRedirect('/surattugas/list/')
    try:
        st_dasar = ST_Dasar()
        #.objects.create(Dasar=DasarSuratTugas.objects.get(dasar=request.POST['dasarnya']),Surat_Tugas=SuratTugas.objects.get(Nomor_Surat=nomorsurat))
        st_dasar.Nomor_Surat = SuratTugas.objects.get(Nomor_Surat=nomorsurat)
        st_dasar.Dasar = DasarSuratTugas.objects.get(dasar=request.POST['dasarnya'])
        st_dasar.save()
    except:
        pass
    return HttpResponseRedirect('/surattugas/create/?surat=' + nomorsurat)

def Exportkan(request):
    try:
        nomorsurat = request.GET['nosur']
    except:
        nomorsurat = None

    if nomorsurat is not None:
        x = docx.Document()
        x.add_heading(nomorsurat,0)
        x.save(os.path.join(settings.BASE_DIR,str(nomorsurat) + '.docx'))

        x = open(os.path.join(settings.BASE_DIR,str(nomorsurat) + '.docx'),'rb')
 
        resp = HttpResponse(x,content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        filename = str(nomorsurat) + '.docx'
        resp['Content-Disposition']='attachment;filename=%s'%format(filename)
        return resp
    else:
        return HttpResponse("nomor surat g ketemu mennnn")
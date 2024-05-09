# from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
# from django.contrib.auth.models import User
from django.db.models import Q
from django.conf import settings
import os
import random
import docx
from docx.shared import Pt,Cm
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
import jwt
from dispenda_surat.models import ExtendUser
from dispenda_surat.serializers import serialUser
import datetime


#for checking jwt exp
def jwt_check(jtw_stream):
    try:
        jwt.decode(jtw_stream,"coba",algorithms="HS256")
        return True
    except:
        return False

def isSuperuser(jtw_stream):
    try:
        is_superuserkah =jwt.decode(jtw_stream,"coba",algorithms="HS256")['token'][0]['is_superuser']
        return is_superuserkah       
    except:
        return False

@api_view(['GET'])
def hello(request):
    return Response({'resp':'Hello World!'})

@api_view(['POST'])
def getJWT(request):
    try:
        data = request.data #membaca body dalam data
        print(data)
        username= data['username']
        password= data['password']
        auth=authenticate(username=username,password=password)
        
        if(auth is not None):
            myfile=open(os.path.join(settings.BASE_DIR,r'static/data/hallo.txt'),'r')
            print(myfile.read())
            user = ExtendUser.objects.all().filter(username=auth)
            serialuser = serialUser(user,many=True)
            data_for_token=serialuser.data
            token = jwt.encode({'token':data_for_token,'exp':datetime.datetime.now(tz=datetime.timezone.utc)+datetime.timedelta(minutes=5),'iat':datetime.datetime.now(tz=datetime.timezone.utc)},'coba',algorithm="HS256")
            return Response({'token':token},status=200)
        else:
            return Response({'token':None},status=401)
    except Exception as ex:
        print(ex)
        return Response({'token':None},status=400)
    
@api_view(['POST'])
def testJWT(request):
    data = request.headers #cek untuk data yang masuk di header bukan body
    token = data['Token']
    check = jwt_check(token)
    if (check):
        return Response({'result':'oke'},status=200)
    else:
        return Response({'result':'expired'},status=401)

@api_view(['PATCH'])
def updateRole(request):
    header = request.headers #membaca headernya
    data = request.data #membaca data
    valid = jwt_check(header['Token']) #cek apakah token jwt valid?

    if(valid):
        superuser = isSuperuser(header['Token']) #jika valid, maka cek apakah superuser
        if(superuser):
            return Response({'result':'super user'},status=200)
        else:
            return Response({'result':'not super user'},status=401)
    else:
        print('token not valid')
        return Response({'result':'token not valid'},status=400)

def getPDF(request):

    pass

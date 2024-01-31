from django.shortcuts import render
from .models import *
from .serailizers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.


@api_view(['GET'])
def getall(request):
    stdata=studinfo.objects.all()
    serial=studserializers(stdata,many=True)
    return Response(data=serial.data)

@api_view(['GET'])
def getid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serial=studserializers(stid)
    return Response(data=serial.data)

@api_view(['DELETE','GET'])
def deleteid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=studserializers(stid)
        return Response(data=serial.data)
    
    if request.method=='DELETE':
        studinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def savedata(request):
    if request.method=='POST':
        stdata=studserializers(data=request.data)
        if stdata.is_valid():
            stdata.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT','GET'])
def updatedata(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=studserializers(stid)
        return Response(data=serial.data)

    if request.method=='PUT':
        stdata=studserializers(data=request.data,instance=stid)
        if stdata.is_valid():
            stdata.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



def home(request):
    url="http://127.0.0.1:8000/"
    req=requests.get(url)
    data=req.json()
    print(data)
    return render(request,'home.html',{'data':data})






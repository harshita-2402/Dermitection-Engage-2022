from django.shortcuts import render, redirect
# from django.shortcuts import render
from .realtimeDetect import DiseaseDetect
from django.core.files.storage import FileSystemStorage




def home(request):
    return render(request, "index.html")

def detection(request):
    context ={}
    context = {'details': DiseaseDetect().detect_disease()}
    return render(request,'index.html', context)

def eyedetect(request):
    context1 = {}
    context1 = {'eyedetails': DiseaseDetect().detect_eyedisease()}
    return render(request,'index.html', context1)
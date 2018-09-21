from django.shortcuts import render
from . import models
from django.http import HttpResponse,FileResponse,Http404
from . import forms
from django.shortcuts import redirect
from JnTkNewApp.models import UserProfile
import operator
from django.core.files.storage import FileSystemStorage
# Create your views here.

def CseView(request):
    if request.method == 'GET':
        data = forms.StudentpostForm(request.POST) 
        bname = request.GET['branchname']
        reg = request.GET['regulation']
        sem = request.GET['semester']
        sname = request.GET['subname']
        uname = request.GET['unit']
        bname = bname.lower()
        reg = reg.lower()
        sname =sname.lower()
        bname =bname.lower()
        try:
            subpdf=models.Branches.objects.filter(branchname=bname,regulation=reg,semester=sem,subname=sname,unit=uname)
            ordered = sorted(subpdf, key=operator.attrgetter('views'),reverse=True)
            videourl=models.videourls.objects.filter(subname=sname)
            ord = sorted(videourl, key=operator.attrgetter('views'),reverse=True)
            return render(request,'out.html',{'object':ordered,'videos':ord})
        except models.Branches.DoesNotExist:
            return HttpResponse("WRONG ENTRIES")    
    else:
        print("HELLO")
        return render(request,'homepage.html')    

def storetodb(request):

    if request.method == 'POST':
        data = forms.postForm(request.POST,request.FILES)
        if data.is_valid():
            p = data.save(commit=False)
            p.teachername = request.user
            k = UserProfile.objects.get(user = request.user)
            p.clgname = k.College_Name
            p.save()
            return redirect('storetodb2')
        else:
            return HttpResponse('Error')    
    else:
        data = forms.postForm()
        return render(request,'trims.html',{'forms':data})    

def storetodb2(request):
    if request.method == 'POST':
        data = forms.urlForm(request.POST,request.FILES)
        if data.is_valid():
            p = data.save(commit=False)
            k = UserProfile.objects.get(user = request.user)
            p.clgname = k.College_Name
            p.save()
            return redirect('storetodb2')
        else:
            return HttpResponse('Error')    
    else:
        data = forms.urlForm()
        return render(request,'trimsnew.html',{'forms':data})    


def CountView(request,slug):
    print(slug)
    print("HELLO")
    data = models.Branches.objects.get(id=slug)
    data.views = data.views + 1
    data.save()
    return HttpResponse("SMILE:))")

def CountViews(request,slug):
    print(slug)
    data = models.videourls.objects.get(id=slug)
    data.views = data.views + 1
    data.save()
    return HttpResponse("SMILE:))")    

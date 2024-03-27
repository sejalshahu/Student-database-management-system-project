from django.http import HttpResponse
from django.shortcuts import render,redirect
from datacollection.models import studentdetail,attendance

def save(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        course=request.POST.get('course')
        joiningdate=request.POST.get('joiningdate')
        duration=request.POST.get('duration')
        rollno=int(request.POST.get('rollno'))

        date=request.POST.get('date')
        topic=request.POST.get('topic')
        intime=request.POST.get('intime')
        outtime=request.POST.get('outtime')
        feedback=request.POST.get('feedback')
        data1=studentdetail(name=name,email=email,course=course,joiningdate=joiningdate,duration=duration,rollno=rollno)
        data2=attendance(date=date,topic=topic,intime=intime,outtime=outtime,feedback=feedback)
        data1.save()
        data2.save()

    return render(request,"dataform.html")

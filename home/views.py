from django.shortcuts import render
from django.http import HttpResponse
from .models import student

# Create your views here.

def home(request):
    results=student.objects.all()
    return render(request,"home/homepage.html",{
        "highlighter":results
    })
 

def success(request,id):
    student_details=student.objects.get(pk=id)
    return render(request,"home/success.html",{
        "student_id":student_details.id,
        "student_name":student_details.name,
        "student_age":student_details.age,
        "student_going_school":student_details.is_going_school
    })


def about(request):
    return render(request,"home/about.html")


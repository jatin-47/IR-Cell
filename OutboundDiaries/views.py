from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def diary(request, year):
    students = out_stu.objects.filter(year=year).order_by('name')
    branches = branch.objects.all()
    return render(request, "OutboundDiaries/diary.html", {
        "year" : year,
        "students" : students,
        "branches" : branches,
        "bool" : 1
    })

def submit(request, year):
    if request.method == 'GET':
        if request.GET['branchID'] == '-1':
            return redirect('diary', year=year)
        else:
            return redirect('filter', year=year, branch_id=request.GET['branchID'])

def filter(request, year, branch_id):
    Branch = branch.objects.get(id=branch_id)
    students = out_stu.objects.filter(year=year,branch=Branch).order_by('name')
    branches = branch.objects.all()
    return render(request, "OutboundDiaries/diary.html", {
        "year" : year,
        "students" : students,
        "branches" : branches,
        "bool" : 1,
        "selected_branch" : branch_id
    })

def student(request, student_id):
    students = out_stu.objects.filter(id=student_id)
    person = out_stu.objects.get(id=student_id)
    interview = person.faq.all()
    return render(request, "OutboundDiaries/diary.html", {
        "year" : person.year,
        "students" : students,
        "interview" : interview,
        "bool" : 0
    })

from django.shortcuts import render,HttpResponse,redirect
from .models import Task,Student

def home(request):
    return render(request,'home.html')


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

def create_task(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        return render(request, 'task/create_task.html',{"tasks":tasks})
    elif request.method == 'POST':
        student = request.POST.get('student')
        title = request.POST.get('title')
        description = request.POST.get('description')
        student = Student.objects.filter(id=student).first()
        Task.objects.create(
            student = student,
            title = title,
            description = description
        )
        return redirect('detail-task-view')

    

def detail_task(request):
    tasks = Task.objects.all()
    return render(request,'task/detail_task.html',{"tasks":tasks})

def delete_task(request,pk):
    tasks = Task.objects.filter(id=pk).first()
    if request.method == 'GET':
        return render(request,'task/delete_task.html',{"data":tasks})
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('detail-task-view')


from datetime import datetime
def update_task(request,pk):
    if request.method == 'GET':
        task = Task.objects.filter(id=pk).first()
        tasks = Task.objects.all()
        return render(request,'task/update_task.html',{"task":task,"tasks":tasks})
    if request.method == 'POST':
        uptask = Task.objects.filter(id=pk).first()
        student_id = request.POST.get('student')
        student = Student.objects.filter(id=student_id).first()
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        uptask.student = student
        uptask.title = title
        uptask.description = description
        uptask.created_at = datetime.now()
        uptask.save()
        return redirect('detail-task-view')
    
    
from django.shortcuts import render,HttpResponse,redirect
from .models import User,Task
def home(request):
    return render(request,'home.html')


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, User

def create_task(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed') == 'on'  # checkbox

        if not user_id or not title or not description:
            return HttpResponse('Error: Please fill all required fields')

        task = Task(
            user_id=user_id,
            title=title,
            description=description,
            is_completed=is_completed
        )
        task.save()
        return redirect('home-view')  # имя URL, не шаблон

    elif request.method == 'GET':
        users = User.objects.all()
        return render(request, 'task/create_task.html', {'users': users})

    

def detail_task(request):
    task = Task.objects.all()
    return render(request,'task/detail_task.html',{"task":task})

def delete_task(request,pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect('task/detail_task.html')
    except Task.DoesNotExist:
        return redirect('task/detail_task.html')
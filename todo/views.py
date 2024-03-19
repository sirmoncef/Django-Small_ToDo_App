from django.shortcuts import render, redirect
from .models import db
from .forms import *

def todo(request):
    tasks = db.objects.all()
    form = Forem()  # Instantiating the form object
    
    if request.method == 'POST':
        form = Forem(request.POST)  
        if form.is_valid():  
            form.save()  # Saving the form data to the database
            return redirect('/')  
    
    context = {'tasks': tasks, 'form': form}
    return render(request, 'base/todo.html', context)

def updateTask(request, pk):
	task = db.objects.get(id=pk)

	form = Forem(instance=task)

	if request.method == 'POST':
		form = Forem(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'base/update_task.html', context)

def deleteTask(request, pk):
	item = db.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'base/delete.html', context)

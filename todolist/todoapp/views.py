from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
# Create your views here.
def todo_home(request):
	if request.method == "POST":
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = List.objects.all
			context = {
				'all_items':all_items,
			}
			messages.success(request, ("Item has been added to List!"))
			return render(request, "todo_home.html", context)
	else:
		all_items = List.objects.all
		context = {
			'all_items':all_items,
		}
		return render(request, "todo_home.html", context)

def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ("Item has been Deleted to List!"))
	return redirect('todo_home')

def cross_off(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('todo_home')

def cross_on(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('todo_home')

def api_view(request):
	all_items = List.objects.all
	context = {
		'all_items':all_items,
	}
	return render(request, "api_todo_home.html", context)

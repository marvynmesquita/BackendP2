from django.shortcuts import render
from django.views import ListView, CreateView
from models import Todo

# Create your views here.
class TodoListView(ListView):
    model = Todo
    template_name = "todo_list.html"

class TodoCreateView(CreateView):
    model = Todo
    template_name = "todo_form.html"


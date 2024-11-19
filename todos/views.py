from django.shortcuts import render
from django.views.generic import CreateView, ListView
from todos.models import Todo
from django.urls import reverse_lazy

# Create your views here.
class TodoListView(ListView):
    model = Todo
    template_name = "todo_list.html"
    fields = ["title", "deadline"]

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title",  "deadline"]
    success_url = reverse_lazy("todo_list")
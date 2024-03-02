from django.shortcuts import render
from django.views.generic import  ListView
from models import Todolist
from forms import TaskForm

# Create your views here.


class ProductsListView(ListView):
    model = Todolist
    template_name = 'index.html'
    context_object_name = 'todolist'
    paginate_by = 6
    form_class = TaskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form_class(self.request.GET)
        return context

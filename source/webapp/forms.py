from django import forms
from models import Todolist


class TaskForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['title', 'description', 'completed', 'created']


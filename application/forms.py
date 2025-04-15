from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'priority','category']  # Specify which fields of the Task model to use in the form
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'priority': forms.Select(choices=Task._meta.get_field('priority').choices),
            'category': forms.Select(choices=Task._meta.get_field('category').choices),
        }
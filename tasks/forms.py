from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'page_type']
        labels = {
            'title': 'Название задачи',
            'page_type': 'Раздел',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Например: Подготовить отчёт...',
                'class': 'form-input'
            }),
            'page_type': forms.Select(attrs={
                'class': 'form-input'
            }),
        }

from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone', 'notes']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone': 'Телефон',
            'notes': 'Заметка',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Например: Таир',
                'class': 'form-input'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Например: Мулаев',
                'class': 'form-input'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+7 (999) 000-00-00',
                'class': 'form-input'
            }),
            'notes': forms.Textarea(attrs={
                'placeholder': 'Кем приходится, адрес или заметка...',
                'rows': 3,
                'class': 'form-input'
            }),
        }

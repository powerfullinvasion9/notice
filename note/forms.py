from django.forms import ModelForm, TextInput, Textarea, Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Note

class AddNote(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['importance'].empty_label = "Статус задачи"

    class Meta:
        model = Note
        fields = ['title','text', 'importance']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control form-control-lg',
                'type': 'text',
                'placeholder': 'Название заметки'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'введите текст'
            }),
            "importance": Select(attrs={
                'class': 'form-select',
            })
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']
from django import forms
from django.forms import ModelForm
from .models import Article

class TestForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your name'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your email'
    }))

# class CommentForm(ModelForm):
#     class Meta:
#         model = Article
#     pass
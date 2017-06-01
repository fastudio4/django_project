from django import forms
from django.forms import ModelForm
from mysite.models import Comments

class TestForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your name'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your email'
    }))

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_text',]

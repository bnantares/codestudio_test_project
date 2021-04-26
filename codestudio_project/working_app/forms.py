from django import forms
from django.core.exceptions import ValidationError


class FeedbackForm(forms.Form):
    '''Форма для отправки feedback email'''
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Ваше имя', 'class': 'text-box', 'id': 'name', 'onfocus': 'blurEvent(this)', 'onkeyup': 'onChangeEvent(this)'}))
    email = forms.EmailField(max_length=250, widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Электронная почта', 'class': 'text-box', 'id': 'email', 'onfocus': 'blurEvent(this)', 'onkeyup': 'onChangeEvent(this)'}))
from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['image', 'title', 'content', 'rate', 'tags']  # убрали 'category'
        widgets = {
            'tags': forms.CheckboxSelectMultiple
        }
        labels = {
            'title': 'Заголовок',
            'content': 'Контент',
            'rate': 'Рейтинг',
            'tags': 'Теги'
        }

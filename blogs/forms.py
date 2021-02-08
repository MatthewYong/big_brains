from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'title',
            'author_friendly',
            'description',
            'date',
            'article',
            'image_url'
        )
"""
        widget = {
            'title': forms.TextInput(attrs={'placeholder': 'Test'})
        }
"""

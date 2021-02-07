from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        article = Blog
        fields = ('title', 'description', 'date',
                  'author', 'story', 'image-url')

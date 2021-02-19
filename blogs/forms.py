from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'title',
            'author_friendly',
            'description',
            'article',
            'image_url',
        )

        labels = {
            "author_friendly": "Author",
        }

        widgets = {
            'image_url': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'https://www.image_url...'}),
            'title': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Title of your Blog'}),
            'author_friendly': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Your name'}),
            'description': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Describe your Blog...'}),
            'article': forms.Textarea(attrs={
                'class': 'textarea', 'rows': 5,
                'placeholder': 'Write your article...'}),
        }

from django import forms
from .models import ToyReview


class ToyReviewForm(forms.ModelForm):
    class Meta:
        model = ToyReview
        fields = (
            'toy',
            'name',
            'comment',
        )

        # Widgets to add placeholders and control layout of the form. Code
        # partially used from: https://www.youtube.com/watch?v=VYs-u0g
        # 1A&t=20s&ab_channel=PrettyPrinted

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Your name'}),
            'comment': forms.Textarea(attrs={
                'class': 'textarea', 'rows': 5,
                'placeholder': 'Write your review...'}),
        }

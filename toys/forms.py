from django import forms
from .models import ToyReview


class ToyReviewForm(forms.ModelForm):
    class Meta:
        model = ToyReview
        fields = (
            'name',
            'comment',
        )

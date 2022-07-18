from django import forms
from .models import ProductReview


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = [
            'rating', 'review_title', 'review_description',
            ]
        
        review_description = forms.CharField(
            widget=forms.Textarea()
        )

from django import forms
from .models import ProductReview


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = [
            'rating', 'review_title', 'review_description',
            ]

        review_description = forms.CharField(
            widget=forms.Textarea(attrs={'rows': '4', 'placeholder': 'Add a review',})
        )

    def __init__(self, *args, **kwargs):
        """ Add classes """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'text-input'

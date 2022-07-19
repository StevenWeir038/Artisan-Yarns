from django import forms
from .models import ProductReview


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = [
            'rating', 'review_title', 'review_description',
            ]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            if field != 'rating':
                self.fields[field].label = False

            placeholders = {
                'rating': 'Rating from 1 to 5 stars...',
                'review_title': 'Give your review a name...',
                'review_description': 'Tell us what you think of this product...',
            }

            placeholder = placeholders[field]
            self.fields['review_description'].widget = forms.Textarea(attrs={'rows': 4,})
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-input'

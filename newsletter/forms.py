from django import forms
from.models import NewsletterSub


class NewsletterSubForm(forms.ModelForm):
    """ Site newsletter form """

    class Meta:
        model = NewsletterSub
        exclude = ('subscribe_date',)

    def __init__(self, *args, **kwargs):
        """
            Add placeholders and classes, remove auto-generated
            labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs[
                'placeholder'] = "Enter your email..."
            self.fields[field].widget.attrs['class'] = 'form-input'
            self.fields[field].label = False

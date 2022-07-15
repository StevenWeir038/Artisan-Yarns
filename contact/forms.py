from django import forms


class ContactForm(forms.Form):
    """ Form to allow site users to communicate with site owners """
    name = forms.CharField(min_length=2, max_length=100, label='Your name')
    email = forms.EmailField(widget=forms.EmailInput(), label='Your Email')
    subject = forms.CharField(min_length=3, max_length=40, label='Subject')
    message = forms.CharField(min_length=5, max_length=300, widget=forms.Textarea(), label='Message')

from django import forms


class ContactForm(forms.Form):
    """ Form to allow site users to communicate with site owners """
    name = forms.CharField(
        min_length=2, max_length=100, label='Your name',required=False)
    email = forms.EmailField(
        widget=forms.EmailInput(), label='Your Email', required=False)
    subject = forms.CharField(
        min_length=3, max_length=40, label='Subject', required=False)
    message = forms.CharField(
        min_length=5, max_length=300, widget=forms.Textarea(),
        label='Message', required=False)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Your Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}*'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-input'
            self.fields[field].label = False

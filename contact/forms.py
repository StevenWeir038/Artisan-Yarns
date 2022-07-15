from django import forms


class ContactForm(forms.ModelForm):
    """
    Form to allow site users to communicate with site owners
    Need get back to user we need a name, email, enquiry subject, message itself
    """

    class Meta:
        


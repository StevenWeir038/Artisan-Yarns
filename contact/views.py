from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm

def contact(request):
    """ Contact page view """
    if request.method == 'POST':
        # create a form instance
        form = ContactForm(request.POST)
    # clean the data

    # if form is valid send the email
    
    # relay a success message to the user

    # if for is not valid create relay a failure message to the user

    # create a blank instance and allow user to repopulate
    else:
        form = ContactForm(request.POST)
    # pass the form to the template via the context dictionary

    template = 'contact/contact.html'
    context = {
        'form': form,
        }

    return render(request, template, context)

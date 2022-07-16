from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    """ Contact page view """
    if request.method == 'POST':
        # create a form instance
        form = ContactForm(request.POST)
        # clean the data
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # if form is valid send the email
            send_mail(
                f'Message from {name}, {email} about {subject}', message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER]
            )
            # relay a success message to the user and redirect to contact page again
            messages.success(request, 'Your message has been sent!')
            # redirect to contact page
            return redirect(reverse('contact'))

        # if form is not valid create relay a failure message to the user. Stay on the same page.
        else:
            messages.error(request, 'There was a problem sending your message. Please try again.')
    # create a blank instance and allow user to repopulate
    else:
        form = ContactForm(request.POST)
    # pass the form to the template via the context dictionary
    template = 'contact/contact.html'
    context = {
        'form': form,
        }

    return render(request, template, context)

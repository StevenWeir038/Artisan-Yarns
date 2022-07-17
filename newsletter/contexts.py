from django.contrib import messages
from .models import NewsletterSub
from .forms import NewsletterSubForm


def subscription_form_contents(request):
    """
    Pass form through context to be available to whole site
    by default.  Essentially this is a view available at site
    level rather than just for app level.
    """
    # POST handler
    if request.method == 'POST':
        # if POST save form to variable
        subscription_form = NewsletterSubForm(request.POST)
        # if data has no issues
        if subscription_form.is_valid():
            # prevent a duplicate email being saved
            instance = subscription_form.save(commit=False)  # don't save the instance
            if Newsletter.objects.filter(email=email).exists():
                # tell the user the email is already on the sub list so do nothing more before exiting loop

            # save the form to the variable
            subscription_form.save()
            # set the variable as the form instance
            subscription_form = NewsletterSubForm()
    else:
        # otherwise just pass an empty form to the context
        subscription_form = NewsletterSubForm()

    context = {
        'subscription_form': subscription_form,
        }

    return context

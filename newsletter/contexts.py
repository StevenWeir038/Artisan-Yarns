from django.contrib import messages
from .models import NewsletterSub
from .forms import NewsletterSubForm


def subscription_form_contents(request):
    """
    Pass form through context to be available to whole site
    by default.  Essentially this is a view available at site
    level rather than just for app level.
    """
    if request.method == 'POST':
        subscription_form = NewsletterSubForm(request.POST)
        if subscription_form.is_valid():
            instance = subscription_form.save(
                commit=False)
            if NewsletterSub.objects.filter(email=instance.email).exists():
                messages.error(request, "You're already subscribed")
            else:
                subscription_form.save()
                subscription_form = NewsletterSubForm()
                messages.success(request, 'Thank you for subscribing')
    else:
        subscription_form = NewsletterSubForm()

    context = {
        'subscription_form': subscription_form,
        }

    return context

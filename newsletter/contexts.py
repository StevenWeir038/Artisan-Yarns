from .models import NewsletterSub
from .forms import NewsletterSubForm


def subscription_form_contents(request):
    """
    Pass form through context to be available to whole site
    by default.  Essentially this is a view available at site
    level rather than just for app level.
    """
    subscription_form = NewsletterSubForm()

    context = {
        'subscription_form': subscription_form,
        }

    return context

from django.db import models

# A newsletter can be as simple as using one field.  In fact the less a user
# has to do to subscribe, the more likely they are to do so.  Therefore, we
# will only ask them to provide their email and click a submit button.


class NewsletterSub(models.Model):
    """
    Newsletter subscription model
    Also add a subscription time.  May be useful in future.
    i.e. Removing old subs programatically after a certain duration.
    Maybe have a new mail autosend each week for 10 weeks (use a counter).
    So many options depending on the business (logic can be worked into view).
    """
    email = models.EmailField()
    subscribe_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Tailor admin display """
        ordering = ['subscribe_date']
        verbose_name_plural = 'Newsletter Subscriptions'

    def __str__(self):
        return self.email

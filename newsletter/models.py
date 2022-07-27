from django.db import models


class NewsletterSub(models.Model):
    """ Newsletter subscription model """
    email = models.EmailField()
    subscribe_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Tailor admin display """
        ordering = ['subscribe_date']
        verbose_name_plural = 'Newsletter Subscriptions'

    def __str__(self):
        return self.email

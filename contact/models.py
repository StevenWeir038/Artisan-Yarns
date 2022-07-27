from django.db import models


class Contact(models.Model):
    """ Contact model """
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=40)
    message = models.TextField(null=True, blank=True)

    class Meta:
        """ Tailor admin display """
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return self.name

from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ ContactAdmin model """
    fields = (
            'name', 'email', 'subject', 'message',
            )
    search_fields = (
        'name', 'email', 'subject', 'message',
        )

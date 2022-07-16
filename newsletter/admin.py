from django.contrib import admin
from .models import NewsletterSub


@admin.register(NewsletterSub)
class NewsletterSubAdmin(admin.ModelAdmin):
    """ NewsletterSubscribeAdmin """
    search_fields = [
        'email', 'subscribe_date'
        ]
    list_display = (
        'email',
        'subscribe_date',
    )
    list_filter = (
        'email', 'subscribe_date',
        )

    ordering = (
        'email', 'subscribe_date'
        )

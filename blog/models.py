
from django.db import models
from wagtail.core.models import Page
# Create your models here.

class BlogListingPage(Page):
    """Listing Page lists all the blog detail pages."""
    custom_title = models.CharField(
        max_length=200, 
        blank=False, 
        null=False, 
        help_text="overwrite default title",
        )
    def get_context(self, request, *args, **kwargs):
        """adding custom stuff to our context."""
        context = super().get_context(request,*args, **kwargs)
        #context['extra'] = 'extra things to display as string in admin page" 
        return context
# class BlogDetailPage(Page):
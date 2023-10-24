"""Resources Page"""

from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

# Create your models here.
class ResourcePage(Page):
    """Resources Page Class"""

    template = "resources/resources_page.html"

    #todo add streamfields 
    # content= StreamField

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),

    ]

    class Meta: #noqa
        verbose_name = "Resources Page"
        verbose_name_plural = "Resources Pages"
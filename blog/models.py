#imports
from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField 
from streams import blocks

# Create your models here.

class BlogListingPage(Page):
    """Listing Page lists all the blog detail pages."""
    custom_title = models.CharField(
        max_length=200, 
        blank=False, 
        null=False, 
        help_text="overwrite default title",
        )
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        """adding custom stuff to our context."""
        context = super().get_context(request,*args, **kwargs)
        #context['extra'] = 'extra things to display as string in admin page" 
        return context
    
class BlogDetailPage(Page):
    """blog detail page"""
    custom_title = models.CharField(
        max_length=200, 
        blank=False, 
        null=False, 
        help_text="overwrite default title",
        )
    blog_image = models.ForeignKey(
        "wagtailimages.Image", 
        blank=False, 
        null=True, 
        related_name="+",
        on_delete= models.SET_NULL, 

    )

    content = StreamField(
        [
            # ("name doesn't matter here", blocks.NAMEOFCLASSinBLOCKS.PY)
            ("author_info", blocks.AuthorInfoBlock()), 
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),

        ],
        #this indicates that all these streamfields are optional
        null=True, 
        blank=True,
    ) 

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("blog_image"),
        StreamFieldPanel("content"),
    ]

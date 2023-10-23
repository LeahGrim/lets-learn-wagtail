from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField 
from streams import blocks

class FlexPage(Page):
    """Flexible Page Class. """

    template = "flex/flex_page.html"

    content = StreamField(
        [
            # ("name doesn't matter here", blocks.NAMEOFCLASSinBLOCKS.PY)
            ("title_and_text", blocks.TitleAndTextBlock()), 
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
            ("button", blocks.ButtonBlock()),

        ],
        #this indicates that all these streamfields are optional
        null=True, 
        blank=True,
    ) 

    subtitle = models.CharField(max_length=10000, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]

    class Meta: #noqa
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"

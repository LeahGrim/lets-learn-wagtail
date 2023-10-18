from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    """Social Media settings for our custom website """
    
    facebook = models.URLfield(blank=True, null=True, help_text="Facebook URL")
    twitter = models.Charfield(blank=True, null=True, help_text="Twitter URL ")
    youtube = models.Charfield(blank=True, null=True, help_text="Youtube Channel")
    
    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"), 
            FieldPanel("youtube"),
        ], heading="Social Media Setting")
    ]
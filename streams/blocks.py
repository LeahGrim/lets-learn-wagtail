"""Streamfield live in here."""
# we are importing blocks.py from wagtail 
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else"""
    
    name = blocks.CharBlock(required=True, help_text='Add your Name')
    info = blocks.TextBlock(required=True, help_text='add info about you here')
    email = blocks.EmailBlock(required=True, help_text ='add your email here for account validation')
    class Meta: 
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Staff Name, Info, Email"   

class CardBlock(blocks.StructBlock):
    """ cards with image and text and button."""
    title = blocks.CharBlock(required=True, help_text='Add your Title')
    
    cards = blocks.ListBlock(
         blocks.StructBlock(
              [
                   ("image", ImageChooserBlock(required=True)), 
                   ("title", blocks.CharBlock(required=True, max_length=40)), 
                   ("text", blocks.TextBlock(required=True, max_length=200)), 
                   ("button_page", blocks.PageChooserBlock(required=False)), 
                   ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first")),
              ]
         )
    )
    class Meta: #noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label= "Owl Cards"


class RichtextBlock(blocks.RichTextBlock):
    """ rich text with all the features. """
    class Meta: 
            template = "streams/richtext_block.html"
            icon = "doc-full"
            label= "Full RichText"

class SimpleRichtextBlock(blocks.RichTextBlock):
    """ rich text without (limited) all the features. """
    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs): #noqa
        super().__init__(**kwargs)
        self.features = [
            "bold", 
            "italic", 
            "link",
            ]
           
    class Meta: 
            template = "streams/richtext_block.html"
            icon = "edit"
            label= "Simple RichText"


class CTABlock(blocks.StructBlock):
     """A simple call to action section."""

     title =  blocks.CharBlock(required=True, max_length=60)
     text = blocks.RichTextBlock(required=True, features= ["bold, italic"])
     button_page = blocks.PageChooserBlock(required=False)
     button_url = blocks.URLBlock(required=False)
     button_text= blocks.CharBlock(required=True, default="Learn More", max_length=50)

     class Meta: #noqa
          template = "streams/cta_block.html"
          icon = "placeholder"
          label = "Call To Action"


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
#author contribution info on blog listing / detail pages         
class AuthorInfoBlock(blocks.StructBlock):
    """Author Info Field Live Here"""
    
    name = blocks.CharBlock(required=True, help_text='Add your Name')
    info = blocks.TextBlock(required=True, help_text='add info about you here')
    email = blocks.EmailBlock(required=True, help_text ='add your email here for account validation')
    author_image = ImageChooserBlock(required=False, help_text="add your photo (optional)")
    
    class Meta: 
        template = "streams/author_info_block.html"
        icon = "edit"
        label = "Author Info" 

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

class LinkStructValue(blocks.StructValue): 
     """Additional logic for our button URLS"""

     def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
             return button_page 
        elif button_url: 
             return button_url 
        return None 
    # adding additional logic to streamfield 
    #  def latest_posts(self):
    #       return BlogDetailPage.objects.live()[:3]

class ButtonBlock(blocks.StructBlock):
     """An external or internal URL."""
     
     button_page = blocks.PageChooserBlock(required=False, help_text='If selected, this url will be used first')
     button_url = blocks.URLBlock(required=False, help_text='If added, this url will be used second to button page')
    
    #adding additional logic to streamfields 
    #  def get_context(self, request, *args, **kwargs):
    #       context = super().get_context(request, *args, **kwargs)
    #       context['latest_posts'] = BlogDetailPage.objects.live().public()[:3]
    #       return context
     
     class Meta: #noqa
          template = "streams/button_block.html"
          icon = "placeholder"
          label = "Single Button"
          value_class = LinkStructValue

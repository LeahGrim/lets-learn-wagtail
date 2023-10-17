
"""Streamfield live in here."""

from wagtail.core import blocks

class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else"""
    
    title = blocks.CharBlock(required=True, help_text='Add your Title')
    text = blocks.TextBlock(required=True, help_text='add additional text here')

    class Meta: 
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"   
        
class RichtextBlock(blocks.RichTextBlock):
    """ rich text with all the features. """
    
    class Meta: 
            template = "streams/richtext_block.html"
            icon = "edit"
            label= "Full RichText"
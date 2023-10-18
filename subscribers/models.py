from django.db import models

# Create your models here.
class Subscribers(models.Model):
    """A subscribers model."""
    email= models.CharField(blank=False, null=False, max_length=100, help_text="email address")
    full_name= models.CharField(blank=False, null=False, max_length=100, help_text="First and Last name")

    def __str__(self):
        """string representation of Subscribers object"""
        return self.full_name
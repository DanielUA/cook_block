from ckeditor.fields import RichTextField
from django.db import models


class ContactModel(models.Model):
    """class model for contacts and messages"""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class ContactLink(models.Model):
    """class model contacts"""
    icon = models.FileField(upload_to="icons/")
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class About(models.Model):
    """Class of model about us"""
    text = RichTextField()
    mini_text = RichTextField()


class ImageAbout(models.Model):
    """Class of model image about us"""
    image = models.ImageField(upload_to="about/")
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name="about_images")
    alt = models.CharField(max_length=100)
class Social(models.Model):
    """Class of model our social site"""
    icon = models.FileField(upload_to="icons/")
    name = models.CharField(max_length=200)
    link = models.URLField()

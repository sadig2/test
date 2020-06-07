from wagtailtrans.models import TranslatablePage
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from django.db import models
from wagtail.core.models import Page



class HomePage(TranslatablePage):
    body = RichTextField(blank=True, default="")
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        ImageChooserPanel('image')
    ]

    subpage_types = [
        # Your subpage types.
    ]
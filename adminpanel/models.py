from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Slider(models.Model):
    image = models.ImageField(upload_to='sliders/')

    title_fr = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    title_ar = models.CharField(max_length=255, blank=True, null=True)

    description_fr = RichTextUploadingField(blank=True, null=True)
    description_en = RichTextUploadingField(blank=True, null=True)
    description_ar = RichTextUploadingField(blank=True, null=True)

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_fr or "Slide"

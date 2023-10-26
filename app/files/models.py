from django.db import models

# Create your models here.


class File(models.Model):
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
    processed = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("File")
        verbose_name_plural = ("Files")

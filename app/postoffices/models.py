from django.db import models
from mixin.assets import TimeStampMixin


# Create your models here.
class PostalAddress(TimeStampMixin):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
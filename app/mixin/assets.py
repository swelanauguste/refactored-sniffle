from django.conf import settings
from django.db import models
from django.views.generic import TemplateView

User = settings.AUTH_USER_MODEL


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name="%(class)s_created_by",
        on_delete=models.SET_DEFAULT, default=1
    )
    updated_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name="%(class)s_updated_by",
        on_delete=models.SET_DEFAULT, default=1,
    )

    class Meta:
        abstract = True




class IndexView(TemplateView):
    template_name = "index.html"

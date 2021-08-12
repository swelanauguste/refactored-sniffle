from django.db import models
from locations.models import District, Community, Quarter
from mixin.assets import TimeStampMixin
from django.urls import reverse
from postoffices.models import PostalAddress


class Nationality(TimeStampMixin):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = 'nationalities'

    def __str__(self):
        return self.name


class Title(TimeStampMixin):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Applicant(TimeStampMixin):
    title = models.ForeignKey(Title, on_delete=models.SET_NULL, null=True)
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    occupation = models.CharField(max_length=100, null=True)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, null=True)
    postal_address = models.ForeignKey(
        PostalAddress, on_delete=models.CASCADE, null=True, blank=True
    )
    community = models.ForeignKey(Community, on_delete=models.SET_NULL, null=True)
    quarter = models.ForeignKey(Quarter, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    home_tel = models.CharField("home", max_length=20, blank=True)
    work_tel = models.CharField("work", max_length=20, blank=True)
    mobile_tel = models.CharField("mobile", max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def get_absolute_url(self):
        return reverse("applicants:applicant-detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        if self.first_name and self.last_name:
            return "%s %s" % (self.first_name, self.last_name)
        return "object %s" % (self.pk)


class IdentificationDocumentType(TimeStampMixin):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


def identification_documents_directory_path(instance, filename):
    return "application_documents/{0}/{1}".format(instance.applicant.id, filename)


class IdentificationDocument(TimeStampMixin):
    applicant = models.ForeignKey(
        Applicant, related_name="applications", on_delete=models.CASCADE
    )
    identification_document_type = models.ForeignKey(
        IdentificationDocumentType,
        related_name="document_types",
        on_delete=models.CASCADE,
    )
    document_no = models.CharField(max_length=25, unique=True)
    document = models.FileField(upload_to=identification_documents_directory_path)

    def __str__(self):
        return self.document_no

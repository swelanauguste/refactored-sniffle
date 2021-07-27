from django.db import models
from mixin.assets import TimeStampMixin
from applicants.models import Applicant
from properties.models import Property


class ApplicationType(TimeStampMixin):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Easement(TimeStampMixin):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class LandUse(TimeStampMixin):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Recommendation(TimeStampMixin):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


def application_documents_directory_path(instance, filename):
    return "application_documents/{0}/{1}".format(instance.id, filename)


class Application(TimeStampMixin):
    application_no = models.CharField(max_length=10)
    file_no = models.CharField(max_length=10)
    date_received = models.DateField()
    applicant = models.ManyToManyField(Applicant)
    plot = models.ForeignKey(Property, on_delete=models.CASCADE)
    application = models.FileField(
        upload_to=application_documents_directory_path, null=True, blank=True
    )
    application_type = models.ManyToManyField(ApplicationType)
    easement = models.ManyToManyField(Easement)
    land_use = models.ManyToManyField(LandUse)
    recommendation = models.ManyToManyField(Recommendation)

    def __str__(self):
        return self.application_no


class Response(TimeStampMixin):
    application = models.ForeignKey(
        Application, related_name="response", on_delete=models.SET_NULL, null=True
    )
    response = models.TextField()

    def __str__(self):
        return self.comment


class Comment(TimeStampMixin):
    application = models.ForeignKey(
        Application, related_name="comments", on_delete=models.SET_NULL, null=True
    )
    comment = models.TextField()

    def __str__(self):
        return self.comment

from django.db import models
from locations.models import Community, Quarter, District
from mixin.assets import TimeStampMixin


class Property(TimeStampMixin):
    parcel = models.CharField(max_length=3)
    block = models.CharField(max_length=5)
    community = models.ForeignKey(Community, on_delete=models.SET_NULL, null=True)
    quarter = models.ForeignKey(Quarter, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    is_queens_chain = models.BooleanField("queen's chain", default=False)

    class Meta:
        verbose_name_plural = 'properties'

    def __str__(self):
        return "%s %s" % (self.parcel, self.block)


class SurveyPlan(TimeStampMixin):
    plot = models.ForeignKey(
        Property, related_name="properties", on_delete=models.SET_NULL, null=True
    )
    survey_plan_no = models.CharField(max_length=100)
    survey_date = models.DateField()

    def __str__(self):
        return self.survey_plan_no

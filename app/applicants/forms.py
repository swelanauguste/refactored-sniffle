from django import forms

from .models import Applicant, IdentificationDocument


class ApplicantCreateForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = "__all__"
        exclude = ["updated_by", "created_by"]


class IdentificationDocumentCreateForm(forms.ModelForm):
    class Meta:
        model = IdentificationDocument
        fields = "__all__"
        exclude = ["updated_by", "created_by"]
from django import forms

from .models import Application


class ApplicationCreateForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = "__all__"
        exclude = ["created_by", "updated_by", "applicant", "plot"]
        widgets = {
            "date_received": forms.DateInput(attrs={"type": "date"}),
        }



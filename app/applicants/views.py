from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormMixin

from .models import Applicant, IdentificationDocument
from .forms import ApplicantCreateForm, IdentificationDocumentCreateForm


class ApplicantCreateView(CreateView):
    model = Applicant
    form_class = ApplicantCreateForm


class ApplicantDetailView(FormMixin, DetailView):
    model = Applicant
    form_class = IdentificationDocumentCreateForm

    def get_initial(self):
        return {"applicant": self.get_object()}

    def get_context_data(self, **kwargs):
        context = super(ApplicantDetailView, self).get_context_data(**kwargs)
        context['identification_documents'] = IdentificationDocument.objects.filter(
            applicant=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.applicant = self.object
        form.save()
        return super(ApplicantDetailView, self).form_valid(form)
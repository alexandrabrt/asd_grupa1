from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie2.models import Companies


# Create your views here.
class CompaniesView(LoginRequiredMixin, ListView):

    model = Companies
    template_name = 'aplicatie2/companies_index.html'


class CreateCompanies(LoginRequiredMixin, CreateView):

    model = Companies
    fields = ['name', 'website', 'company_type', 'location']
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('aplicatie2:lista_companii')


class UpdateCompanies(LoginRequiredMixin, UpdateView):

    model = Companies
    fields = ['name', 'website', 'company_type', 'location']
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('aplicatie2:lista_companii')

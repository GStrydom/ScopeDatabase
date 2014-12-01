from django.shortcuts import render_to_response

from django.views.generic import ListView, DetailView

from .models import Client, Clientinformation


class ClientListView(ListView):
    template_name = 'lists.html'
    model = Client

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        return context


class ClientInformationView(DetailView):
    template_name = 'detail.html'
    model = Clientinformation

    def get_context_data(self, **kwargs):
        context = super(ClientInformationView, self).get_context_data(**kwargs)
        return context
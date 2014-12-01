from django.views.generic import ListView, DetailView

from .models import Customer, Customerinformation


class CustomerListView(ListView):
    template_name = 'lists.html'
    model = Customer

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        return context


class CustomerInformationView(DetailView):
    template_name = 'detail.html'
    model = Customerinformation

    def get_context_data(self, **kwargs):
        context = super(CustomerInformationView, self).get_context_data(**kwargs)
        return context
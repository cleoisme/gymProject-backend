from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Address


class AddressListView(ListView):
    model = Address
    template_name = "address/address_list.html"  # Replace with your actual template


class AddressDetailView(DetailView):
    model = Address
    template_name = "address/address_detail.html"  # Replace with your actual template


class AddressCreateView(CreateView):
    model = Address
    template_name = "address/address_form.html"  # Replace with your actual template
    fields = "__all__"


class AddressUpdateView(UpdateView):
    model = Address
    template_name = "address/address_form.html"  # Replace with your actual template
    fields = "__all__"


class AddressDeleteView(DeleteView):
    model = Address
    template_name = (
        "address/address_confirm_delete.html"  # Replace with your actual template
    )
    success_url = reverse_lazy("address-list")

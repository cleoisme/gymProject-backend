from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import AppointmentType, Appointment


class AppointmentTypeListView(ListView):
    model = AppointmentType
    template_name = "appointments/appointmenttype_list.html"


class AppointmentTypeDetailView(DetailView):
    model = AppointmentType
    template_name = "appointments/appointmenttype_detail.html"


class AppointmentCreateView(CreateView):
    model = Appointment
    template_name = "appointments/appointment_form.html"
    fields = "__all__"


class AppointmentUpdateView(UpdateView):
    model = Appointment
    template_name = "appointments/appointment_form.html"
    fields = "__all__"


class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = "appointments/appointment_confirm_delete.html"
    success_url = reverse_lazy("appointment-list")

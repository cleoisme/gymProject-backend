from django.shortcuts import redirect, render, get_object_or_404
from gymCMS.models.appointment import Appointment, AppointmentType


def list_all_appointment_types(request):
    appointment_types = AppointmentType.objects.all()
    return render(
        request, "appointment_type_list.html", {"appointments": appointment_types}
    )


def show_appointment_type_details(request, appointment_type_id):
    # address = AppointmentType.objects.get(pk=appointment_type_id)
    appointment_type = get_object_or_404(AppointmentType, pk=appointment_type_id)
    return render(
        request, "appointment_type_details.html", {"appointment_type": appointment_type}
    )


def create_an_appointment_type(request):
    if request.method == "POST":
        # TODO: Parse the payload
        new_appointment_type = Appointment(request.POST)
        if new_appointment_type.is_valid():
            new_appointment_type.save()
            return redirect(
                "appointment_type_create.html",
                appointment_type_id=new_appointment_type.id,
            )
    else:
        new_appointment_type = Appointment()
    return render(
        request,
        "appointment_type_create.html",
        {"appointment_type": new_appointment_type},
    )


def list_all_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, "appointment_list.html", {"appointments": appointments})


def show_an_appointment(request, appointment_id):
    # address = Appointment.objects.get(pk=appointment_id)
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, "appointment_details.html", {"appointment": appointment})


# Create function for Appointment
def create_an_appointment(request):
    if request.method == "POST":
        # TODO: Parse the payload
        new_appointment = Appointment(request.POST)
        if new_appointment.is_valid():
            new_appointment.save()
            return redirect(
                "appointment_create.html", appointment_id=new_appointment.id
            )
    else:
        new_appointment = Appointment()
    return render(request, "appointment_create.html", {"appointment": new_appointment})


# Update function for Appointment
def update_an_appointment(request, appointment_id):
    # address = Appointment.objects.get(pk=appointment_id)
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == "POST":
        # TODO: Parse the payload
        new_appointment = Appointment(request.POST, instance=appointment)
        if new_appointment.is_valid():
            new_appointment.save()
            return redirect("appointment_update.html", appointment_id=appointment.id)
    else:
        new_appointment = Appointment()
    return render(request, "appointment_update.html", {"appointment": new_appointment})


# Delete function for Appointment
def delete_an_appointment(request, appointment_id):
    # address = Appointment.objects.get(pk=appointment_id)
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == "POST":
        appointment.delete()
        return redirect("appointment_delete.html")
    return render(request, "appointment_delete.html", {"appointment": appointment})

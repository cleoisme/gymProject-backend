from django.core.serializers import serialize
from django.shortcuts import redirect, render, get_object_or_404
from gymCMS.models.appointment import Appointment, AppointmentType


def list_all_appointment_types(request):
    appointment_types = AppointmentType.objects.all()
    appointment_types_data = serialize("json", appointment_types)
    return render(
        request,
        "appointment_type_list.html",
        {"appointment_types": appointment_types_data},
    )


def show_appointment_type_details_by_id(request):
    appointment_type_id = request.GET.get("appointment_type_id")
    if appointment_type_id is not None:
        appointment_type = get_object_or_404(AppointmentType, pk=appointment_type_id)
        appointment_type_data = serialize("json", appointment_type)
        return render(
            request,
            "appointment_type_details.html",
            {"appointment_type": appointment_type_data},
        )
    else:
        return render(request, "NOT_FOUND.html", {"Items Not Found"})


def create_an_appointment_type(request):
    new_appointment_type = None
    if request.method == "POST":
        new_appointment_type = AppointmentType(request.POST)
        if new_appointment_type.is_valid():
            new_appointment_type_data = serialize("json", new_appointment_type)
            new_appointment_type.save()
            return render(
                request,
                "appointment_type_create.html",
                {"appointment_type": new_appointment_type_data},
            )


def list_all_appointments(request):
    appointments = Appointment.objects.all()
    appointments_data = serialize("json", appointments)
    return render(request, "appointment_list.html", {"appointments": appointments_data})


def show_an_appointment_by_id(request):
    appointment_id = request.GET.get("appointment_id")
    if appointment_id is not None:
        appointment = get_object_or_404(Appointment, pk=appointment_id)
        appointment_data = serialize("json", appointment)
        return render(
            request, "appointment_details.html", {"appointment": appointment_data}
        )
    else:
        return render(request, "NOT_FOUND.html", {"Items Not Found"})


# Create function for Appointment
def create_an_appointment(request):
    new_appointment = None
    if request.method == "POST":
        new_appointment = Appointment(request.POST)
        if new_appointment.is_valid():
            new_appointment_data = serialize("json", new_appointment)
            new_appointment.save()
            return render(
                request,
                "appointment_create.html",
                {"appointment": new_appointment_data},
            )


# Update function for Appointment
def update_an_appointment(request):
    appointment_id = request.PUT.get("appointment_id")
    if appointment_id is not None:
        appointment = get_object_or_404(Appointment, pk=appointment_id)
        new_appointment = Appointment(request.PUT, instance=appointment)
        if new_appointment.is_valid():
            new_appointment.save()
            return redirect("appointment_update.html", {"appointment": new_appointment})
        else:
            new_appointment = Appointment(request.PUT)

    return render(request, "NOT_FOUND.html.html", {"Items Not Found"})


# Delete function for Appointment
def delete_an_appointment(request):
    if request.method == "POST":
        appointment_id = request.POST.get("appointment_id")
        if appointment_id is not None:
            appointment = get_object_or_404(Appointment, pk=appointment_id)
            appointment.delete()
            return redirect("appointment_delete.html")
    return render(request, "NOT_FOUND.html.html", {"Items Not Found"})

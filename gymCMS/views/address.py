from django.core.serializers import serialize
from django.shortcuts import redirect, render, get_object_or_404
from gymCMS.models.address import Address


def list_all_addresses(request):
    addresses = Address.objects.all()
    addresses_data = serialize("json", addresses)

    return render(request, "address_list.html", {"addresses": addresses_data})


def show_address_details_by_id(request):
    address_id = request.GET.get("address_id")
    if address_id is not None:
        address = get_object_or_404(Address, pk=address_id)
        address_data = serialize("json", address)
        return render(request, "address_details.html", {"address": address_data})
    else:
        return render(request, "NOT_FOUND.html", {"Items Not Found"})


def create_an_address(request):
    new_address = None
    if request.method == "POST":
        new_address = Address(request.POST)
        if new_address.is_valid():
            new_addresses_data = serialize("json", new_address)
            new_address.save()
            return render(
                request, "address_create.html", {"address": new_addresses_data}
            )


def update_an_address(request):
    address_id = request.PUT.get("address_id")
    if address_id is not None:
        address = get_object_or_404(Address, pk=address_id)
        new_address = Address(request.PUT, instance=address)
        if new_address.is_valid():
            new_address.save(address_id)
            return redirect("address_update.html", {"address": new_address})
    else:
        new_address = Address(request.PUT)

    return render(request, "NOT_FOUND.html.html", {"Items Not Found"})


def delete_an_address(request):
    if request.method == "POST":
        address_id = request.POST.get("address_id")
        if address_id is not None:
            address = get_object_or_404(Address, pk=address_id)
            address.delete()
            return redirect("address_delete.html")

    return render(request, "NOT_FOUND.html.html", {"Items Not Found"})

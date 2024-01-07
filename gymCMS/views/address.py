from django.shortcuts import redirect, render, get_object_or_404

from gymCMS.models.address import Address


def list_all_addresses(request):
    addresses = Address.objects.all()
    return render(request, "address_list.html", {"addresses": addresses})


def show_address_details_by_id(request, address_id):
    # address = Address.objects.get(pk=address_id)
    address = get_object_or_404(Address, pk=address_id)
    return render(request, "address_details.html", {"address": address})


def create_an_address(request):
    if request.method == "POST":
        # TODO: Parse the data load
        new_address = Address(request.POST)
        # TODO: Validate the address
        if new_address.is_valid():
            new_address.save()
            return redirect(
                "user_profile"
            )  # Redirect to the user profile where address is updated to after successful creation
    else:
        new_address = Address()
    return render(request, "address_create.html", {"address": new_address})


def update_an_address(request, address_id):
    # address = Address.objects.get(pk=address_id)
    address = get_object_or_404(Address, pk=address_id)
    if request.method == "POST":
        new_address = Address(request.POST, instance=address)
        if new_address.is_valid():
            new_address.save(address_id)
            return redirect(
                "user_profile"
            )  # Redirect to the user profile where address is updated to after successful creation
    else:
        address = Address()
    return render(request, "address_update.html", {"address": new_address})


def delete_an_address(request, address_id):
    # address = Address.objects.get(pk=address_id)
    address = get_object_or_404(Address, pk=address_id)
    if request.method == "POST":
        address.delete_by_id(address_id)
        return redirect(
            "user_profile"
        )  # Redirect to the user profile where address is updated to after successful creation
    return render(request, "address_delete.html", {"address": address})

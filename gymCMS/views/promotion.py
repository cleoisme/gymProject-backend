from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from gymCMS.models.promotion import Promotion


def list_all_promotions(request):
    promotions = Promotion.objects.all()
    promotions_data = serialize("json", promotions)

    return render(request, "promotion_list.html", {"promotions": promotions_data})


def show_promotion_details_by_id(request):
    promotion_id = request.GET.get("promotion_id")
    if promotion_id is not None:
        promotion = get_object_or_404(Promotion, pk=promotion_id)
        promotion_data = serialize("json", promotion)
        return render(request, "promotion_details.html", {"promotion": promotion_data})
    else:
        return render(request, "NOT_FOUND.html", {"Items Not Found"})


def create_a_promotion(request):
    new_promotion = None
    if request.method == "POST":
        new_promotion = Promotion(request.POST)
        if new_promotion.is_valid():
            new_promotion_data = serialize("json", new_promotion)
            new_promotion.save()
            return render(
                request, "promotion_create.html", {"promotion": new_promotion_data}
            )


def update_a_promotion(request):
    promotion_id = request.PUT.get("promotion_id")
    if promotion_id is not None:
        promotion = get_object_or_404(Promotion, pk=promotion_id)
        new_promotion = Promotion(request.POST, instance=promotion)
        if new_promotion.is_valid():
            new_promotion.save()
            return redirect("promotion_update.html", {"promotion": new_promotion})
    else:
        new_promotion = Promotion(request.PUT)

    return render(request, "NOT_FOUND.html.html", {"Items Not Found"})


def delete_a_promotion(request):
    if request.method == "POST":
        promotion_id = request.POST.get("promotion_id")
        if promotion_id is not None:
            promotion = get_object_or_404(Promotion, pk=promotion_id)
            promotion.delete()
            return redirect("promotion_delete.html")
    return render(request, "NOT_FOUND.html.html", {"Items Not Found"})

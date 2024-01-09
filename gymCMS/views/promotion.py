from django.shortcuts import get_object_or_404, redirect, render
from gymCMS.models.promotion import Promotion


def list_all_promotions(request):
    promotions = Promotion.objects.all()
    return render(request, "promotion_list.html", {"promotions": promotions})


def show_promotion_details_by_id(request, promotion_id):
    promotion = get_object_or_404(Promotion, pk=promotion_id)
    return render(request, "promotion_details.html", {"promotion": promotion})


def create_a_promotion(request):
    if request.method == "POST":
        new_promotion = Promotion(request.POST)
        if new_promotion.is_valid():
            new_promotion.save()
            return redirect("promotion_list")  # Redirect to the promotion list view
    else:
        new_promotion = Promotion()
    return render(request, "create_promotion.html", {"promotion": new_promotion})


def update_a_promotion(request, promotion_id):
    promotion = get_object_or_404(Promotion, pk=promotion_id)
    if request.method == "POST":
        new_promotion = Promotion(request.POST, instance=promotion)
        if new_promotion.is_valid():
            new_promotion.save()
            return redirect("promotion_list")  # Redirect to the promotion list view
    else:
        new_promotion = Promotion(instance=promotion)
    return render(request, "update_promotion.html", {"promotion": new_promotion})


def delete_a_promotion(request, promotion_id):
    promotion = get_object_or_404(Promotion, pk=promotion_id)
    if request.method == "POST":
        promotion.delete()
        return redirect("promotion_list")  # Redirect to the promotion list view
    return render(request, "delete_promotion.html", {"promotion": promotion})

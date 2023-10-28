from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Promotion


class PromotionListView(ListView):
    model = Promotion
    template_name = "promotion/promotion_list.html"  # Replace with your actual template


class PromotionDetailView(DetailView):
    model = Promotion
    template_name = (
        "promotion/promotion_detail.html"  # Replace with your actual template
    )


class PromotionCreateView(CreateView):
    model = Promotion
    template_name = "promotion/promotion_form.html"  # Replace with your actual template
    fields = "__all__"


class PromotionUpdateView(UpdateView):
    model = Promotion
    template_name = "promotion/promotion_form.html"  # Replace with your actual template
    fields = "__all__"


class PromotionDeleteView(DeleteView):
    model = Promotion
    template_name = (
        "promotion/promotion_confirm_delete.html"  # Replace with your actual template
    )
    success_url = reverse_lazy("promotion-list")

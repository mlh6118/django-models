from django.views.generic import ListView, DetailView
from .models import Snack


class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = 'list_of_snacks'


class SnackDetail(DetailView):
    template_name = "snack_detail.html"
    model = Snack
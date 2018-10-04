from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Picture


class AllPicturesView(ListView):
    model = Picture
    paginate_by = 20


class AddPictureView(CreateView):
    model = Picture
    fields = ['title', 'image']

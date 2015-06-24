from django.views.generic.list import ListView
from scratchers.models import Scratcher


class ScratchersList(ListView):
    model = Scratcher
    template_name = 'scratchers/scratchers_list.html'
    context_object_name = 'scratchers'

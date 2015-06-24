from django.conf.urls import url
from scratchers.views import ScratchersList

urlpatterns = [
    url(r'list/$', ScratchersList.as_view(), name='scratchers-list')
]

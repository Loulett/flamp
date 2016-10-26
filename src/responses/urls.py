from django.conf.urls import url
from .views import ResponsesList, ResponseView

urlpatterns = [
    url(r'^$', ResponsesList.as_view(), name='response_list'),
    url(r'^(?P<pk>\d+)/$', ResponseView.as_view(), name='resp'),
]
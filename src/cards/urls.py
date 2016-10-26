from django.conf.urls import url
from .views import CardList, CardView

urlpatterns = [
    url(r'^$', CardList.as_view(), name='cards_list'),
    url(r'^(?P<pk>\d+)/$', CardView.as_view(), name='card'),
]
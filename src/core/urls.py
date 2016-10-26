from django.conf.urls import url
from .views import UserList, UserView

urlpatterns = [
    url(r'^$', UserList.as_view(), name='user_list'),
    url(r'^(?P<pk>\d+)/$', UserView.as_view(), name='user'),
]
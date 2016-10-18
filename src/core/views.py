from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import User


class UserView(DetailView):
    model = User
    template_name = 'core/user.html'


class UserList(ListView):
    model = User
    template_name = 'core/users_list.html'
    context_object_name = 'users_list'


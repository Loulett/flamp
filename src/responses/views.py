from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Response


class ResponseView(DetailView):
    model = Response
    template_name = 'responses/response.html'


class ResponsesList(ListView):
    model = Response
    template_name = 'responses/responses_list.html'

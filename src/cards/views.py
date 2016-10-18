from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Card


class CardView(DetailView):
    model = Card
    template_name = 'cards/card.html'


class CardList(ListView):
    model = Card
    template_name = 'cards/cards_list.html'

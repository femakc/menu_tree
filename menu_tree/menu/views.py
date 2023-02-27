from django.shortcuts import render
from .models import Menu


def index(request):
    template = 'menu/index.html'
    prod_name = 'menu_tree'
    items = Menu.objects.all()
    context = {
        'template': template,
        'prod_name': prod_name,
        'items': items,
    }
    return render(request, template, context)

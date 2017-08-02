from django.http import HttpResponse
from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST.get('item_text', ''))
        return redirect('/lists/theonlylistintheworld/')

    items = Item.objects.all()

    return render(request, 'home.html', {'items': items})

def view_list(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

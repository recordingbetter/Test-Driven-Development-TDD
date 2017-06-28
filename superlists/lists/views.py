from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item


def home_page(request):
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # return render(request, 'lists/home.html')
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()

    if request.method == 'POST':
        # new_item_text = request.POST['item_text']
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    # else:
    #     new_item_text = ''

    items = Item.objects.all()
    context = {
        'items': items,
        }
    return render(request, 'lists/home.html', context)


from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image
# Create your views here.

def photos(request):
    images = Image.all_images()
    return render(request, 'index.html', {"images":images})

def search(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request,'search.html',{"images":searched_images,"category":search_term,"message":message})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

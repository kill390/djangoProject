from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic.list import ListView
from .models import Count

# Create your views here.
class CountListView(ListView):
    context_object_name = 'count_list'
    template_name = 'my_site/index.html'
    model = Count

def count(Request, count_id):
    try:
        c = Count.objects.get(pk=count_id)
    except:
        return Http404("Count not found")

    return HttpResponse("<script> alert('The current Counter: " + str(c.counter) + "') </script>")

def delete(Request, count_id):
    return HttpResponse()

def update(Request, count_id):
    return HttpResponse()
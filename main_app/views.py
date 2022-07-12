

from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Business
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

def home(request):
    # return HttpResponse('<h1>Hello</h1>')
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def businesses_index(request):
    businesses = Business.objects.all()
    return render(request, 'businesses/index.html', {'businesses': businesses})

def businesses_detail(request, business_id):
    business = Business.objects.get(id=business_id)
    return render(request, 'businesses/detail.html', { 'business' : business })


class BusinessCreate(CreateView):
    model = Business
    fields = '__all__'
    success_url = '/businesses/'

class BusinessUpdate(UpdateView):
    model = Business
    fields = '__all__'

class BusinessDelete(DeleteView):
    model = Business
    success_url = '/businesses/'
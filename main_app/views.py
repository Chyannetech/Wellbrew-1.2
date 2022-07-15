from django.shortcuts import render, redirect
from .models import Business
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    # return HttpResponse('<h1>Hello</h1>')
    return render(request, 'home.html')

def directory(request):
    return render(request, 'directory.html')

@login_required
def businesses_index(request):
    businesses = Business.objects.filter(user=request.user)
    return render(request, 'businesses/index.html', {'businesses': businesses})

@login_required
def businesses_detail(request, business_id):
    business = Business.objects.get(id=business_id)
    return render(request, 'businesses/detail.html', { 'business' : business })


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class BusinessCreate(LoginRequiredMixin, CreateView):
    model = Business
    fields = ['name', 'address', 'phone', 'social', 'website']
    success_url = '/businesses/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BusinessUpdate(LoginRequiredMixin, UpdateView):
    model = Business
    fields = '__all__'

class BusinessDelete(LoginRequiredMixin, DeleteView):
    model = Business
    success_url = '/businesses/'
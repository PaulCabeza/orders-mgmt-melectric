from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import MyCustomUserCreationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = MyCustomUserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')

    else:
        form = MyCustomUserCreationForm()

    
    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)
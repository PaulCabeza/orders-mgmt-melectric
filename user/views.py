from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import MyCustomUserCreationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = MyCustomUserCreationForm(request.POST)
        # form.clean_email(request.POST['email'])
        if form.is_valid:
            # form.clean_email()
            form.save()
            return redirect('login')

    else:
        form = MyCustomUserCreationForm()

    
    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)
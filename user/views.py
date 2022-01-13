from django.contrib import messages
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
            messages.success(request, 'New user created successfully.')
            return redirect('login')

        else:
            messages.error(request, 'Something wrong happened, please try again.')
            return redirect('login')

    else:
        form = MyCustomUserCreationForm()

    
    context = {
        'form': form,
        'messages': messages
    }
    return render(request, 'user/register.html', context)
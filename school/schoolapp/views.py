from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View
from django.urls import path
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect

from .signup import SignupForm

def index(request):
        return render(request, 'schoolapp/index.html')

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email_address')
        message = request.POST.get('message')

        send_mail(
            f'Contact Form Submission from {name}',
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        return HttpResponse('Thank you for your message.')
    else:
        return render(request, 'schoolapp/contact_form.html')
    
def newsletter_signup(request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email_address')
        password = request.POST.get('password')

        # NewsletterSignup.objects.create(name=name, email=email, password=password)

        return HttpResponse('Thank you for signing up for our newsletter.')
    else:
        return render(request, 'schoolapp/newsletter_signup.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

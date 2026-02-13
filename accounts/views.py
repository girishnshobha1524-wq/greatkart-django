from django.shortcuts import render
from .forms import RegistrationForm
from .models import Accounts
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name   = form.cleaned_data['first_name']
            last_name    = form.cleaned_data['last_name']
            email        = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password     = form.cleaned_data['password']
            username     = email.split('@')[0]
            
            user = Accounts.objects.create_user(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, password=password, username=username)
            user.phone_number = phone_number
            user.save()
            
            # USER ACTIVATION
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),      
            })
            to_email = email
            send_mail(mail_subject, message, settings.DEFAULT_FROM_EMAIL, [to_email])
            
            messages.success(request, 'Registered successfully !')
            return redirect('register')
            to_email = email
            send_mail = EmailMessage(mail_subjecct, message, to=[to_email])
            send_mail.send()
            
    else:
        form = RegistrationForm()
    
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You are logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout(request):  
    auth.logout(request)
    messages.success(request, 'You are logged out !')
    return redirect('login')
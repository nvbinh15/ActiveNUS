from django.shortcuts import render, redirect
from django.contrib import messages
from validate_email import validate_email
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from helpers.decorators import auth_user_should_not_access
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
import threading

# Create your views here.


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()



def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'ActiveNUS | Activate your account'
    email_body = render_to_string('authentication/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token':generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                    from_email=settings.EMAIL_FROM_USER, to=[user.email]
                    )
    

    EmailThread(email).start()




@auth_user_should_not_access
def login_user(request):

    if request.method == "POST":
        context = {'data': request.POST}
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if not user:
            messages.add_message(request, messages.ERROR,
                                'Invalid credentials')
            return render(request, 'authentication/login.html', context)

        if not user.is_email_verified:
            messages.add_message(request, messages.ERROR,
                            'Email is not verified, please check your email inbox')
            return render(request, 'authentication/login.html', context, status=401)

        login(request, user)

        
        return redirect(reverse('home'))

    return render(request, 'authentication/login.html')


@auth_user_should_not_access
def register(request):
    if request.method == "POST":
        context = {'has_error': False, 'data': request.POST}
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if len(username) > 150:
            messages.add_message(request, messages.ERROR,
                            'Username should contain 150 characters or fewer')
            context['has_error'] = True

        if len(password1) < 8:
            messages.add_message(request, messages.ERROR,
                                 'Password should be at least 8 characters')
            context['has_error'] = True

        if password1 != password2:
            messages.add_message(request, messages.ERROR,
                                 'Password mismatch')
            context['has_error'] = True
            
            return render(request, 'authentication/register.html', context, status=409)

        if not validate_email(email):
            messages.add_message(request, messages.ERROR,
                                 'Enter a valid email address')
            context['has_error'] = True

        if not username:
            messages.add_message(request, messages.ERROR,
                                 'Username is required')
            context['has_error'] = True

        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR,
                                 'Username is taken, choose another one')
            context['has_error'] = True

            return render(request, 'authentication/register.html', context, status=409)

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 'Email is taken, choose another one')
            context['has_error'] = True

            return render(request, 'authentication/register.html', context, status=409)

        if context['has_error']:
            return render(request, 'authentication/register.html', context)

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password1)
        user.save()


        if not context['has_error']:
            send_activation_email(user, request)

            messages.add_message(request, messages.SUCCESS,
                             'We sent you an email to verify your account')
            return redirect('auth_login')

    return render(request, 'authentication/register.html')


def logout_user(request):

    logout(request)

    messages.add_message(request, messages.SUCCESS,
                         'Successfully logged out')

    return redirect(reverse('auth_login'))


def activate_user(request, uidb64, token):

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             'Email verified, you can now login')
        return redirect(reverse('auth_login'))

    return render(request, 'authentication/activate-failed.html', {"user": user})
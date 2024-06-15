from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('Hello from UNSA',
              'Hello there. This is an automated message',
              'hz@outlook.com.pe',
              ['vadej41229@fna6.com'],
              fail_silently=False)

    return render(request, 'index.html')
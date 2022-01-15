from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from .models import Querie, Product
from requests.packages import urllib3
urllib3.disable_warnings()
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'


# Create your views here.
def index(request):
    id = Product.objects.filter(Active=True)[:6]
    return render(request, 'index.html',{'products': id})


def contact(request):
    return render(request, 'contact.html')


def enquiry(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        data = Querie(Name=name, Email=email, Phone=phone, Message=message)
        data.save()
        send_mail(
            'Thanks for Submitting your enquiry to us.',
            'Our Representative will be in contact with you soon.',
            'info@sapacares.com',
            [email],
            fail_silently=True,
        )
        send_mail(
            'Query from '+ name,
            'Email: '+email+'\nPhone: '+phone+'\nMessage: '+message,
            'info@sapacares.com',
            ['info@sapacares.com'],
            fail_silently=True,
        )
        messages.error(request, "Our representative will Contact you shortly.")
        return redirect('index')
    return render(request, 'enquiry.html')


def products(request):
    id = Product.objects.filter(Active=True)
    return render(request, 'OurProducts.html', {'products': id})


def about(request):
    return render(request, 'about.html')


def product(request, sno):
    if Product.objects.filter(sno=sno):
        id = Product.objects.get(sno=sno)
        Features = id.Features.split(';')
        Instructions = id.Instructions.split(';')
        data = {"product": id, 'Feature': Features, 'Instruction': Instructions}
        return render(request, 'Product.html', data)
    else:
        return redirect("index")

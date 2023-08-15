from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import *


# Create your views here.
def home(request):
    landing = Home.objects.all()
    about = About.objects.all()
    competency = Competency.objects.all()
    portfolios = Portfolio.objects.exclude(id=1)  # Exclude the Portfolio with id 1
    tech = PortfolioTech.objects.filter(portfolio__in=portfolios)
    services = Services.objects.all()
    contact = Contact.objects.get(id=1)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send the email
        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            settings.DEFAULT_FROM_EMAIL,  # Use the default email address configured in settings.py
            ['mosessampson21@gmail.com'],  # Replace with the recipient's email address(es)
            fail_silently=False,
        )

    return render(request, 'home/index.html', {
        'homes': landing,
        'abouts': about,
        'competencys': competency,
        'portfolios': portfolios,
        'Techs': tech,
        'services': services,
        'contact': contact
    })


def portfolio(request, pk):
    port = Portfolio.objects.get(id=pk)
    portfolio_tech = port.p_tech.all()
    contact = Contact.objects.get(id=1)
    img_p = port.p_image.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send the email
        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            settings.DEFAULT_FROM_EMAIL,  # Use the default email address configured in settings.py
            ['mosessampson21@gmail.com'],  # Replace with the recipient's email address(es)
            fail_silently=False,
        )

    return render(request, 'home/portfolio.html', {'portfolio': port, 'tech': portfolio_tech,
                                                   'contact': contact, 'images_p': img_p})


def service(request, pk):
    sev = Services.objects.get(id=pk)
    services = sev.s_text.all()
    img = sev.s_image.all()
    contact = Contact.objects.get(id=1)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send the email
        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            settings.DEFAULT_FROM_EMAIL,  # Use the default email address configured in settings.py
            ['mosessampson21@gmail.com'],  # Replace with the recipient's email address(es)
            fail_silently=False,
        )

    return render(request, 'home/services.html',
                  {'service': sev, 'services': services, 'services_image': img, 'contact': contact})

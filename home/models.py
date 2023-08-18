from django.db import models
from django.forms import inlineformset_factory


# Create your models here.
class Home(models.Model):
    first_text = models.CharField(max_length=20)
    second_text = models.CharField(max_length=20)

    def __str__(self):
        return 'Landing Page Text'


class About(models.Model):
    about_image = models.ImageField(upload_to='images/')
    about_text = models.TextField()

    def __str__(self):
        return 'About'


class Competency(models.Model):
    competency_image = models.ImageField(upload_to='images/Competency/')
    competency_text = models.CharField(max_length=50)

    def __str__(self):
        return self.competency_text


class Portfolio(models.Model):
    portfolio_summary = models.CharField(max_length=100)
    portfolio_image = models.ImageField(upload_to='images/Portfolio/')
    portfolio_source = models.URLField()
    portfolio_about = models.TextField()

    def __str__(self):
        return self.portfolio_summary


class PortfolioTech(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='p_tech')
    portfolio_tech = models.CharField(max_length=50)

    def __str__(self):
        return 'Portfolio Tech'


class PortfolioImages(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='p_image')
    portfolio_img = models.ImageField(upload_to='images/Portfolio/')


class Services(models.Model):
    service_icon = models.ImageField(upload_to='images/Services/Icon/', default='logo.png')
    service_text = models.CharField(max_length=20, default='None')
    service_image = models.ImageField(upload_to='images/Services/', default='logo.png')

    def __str__(self):
        return self.service_text


class ServicesText(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='s_text')
    services = models.CharField(max_length=200)

    def __str__(self):
        return 'Services Text'


class ServicesImage(models.Model):
    service_im = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='s_image')
    img_s = models.ImageField(upload_to='images/Services/')


class Contact(models.Model):
    twitter = models.URLField()
    facebook = models.URLField()
    Linkedin = models.URLField()
    Instagram = models.URLField()
    tiktok = models.URLField()
    github = models.URLField()
    upwork = models.URLField()
    fiverr = models.URLField()

    def __str__(self):
        return 'Contact'


PortfolioTechFormSet = inlineformset_factory(Portfolio, PortfolioTech, fields=('portfolio_tech',), extra=1)
PortfolioImageFormSet = inlineformset_factory(Portfolio, PortfolioImages, fields=('portfolio_img',), extra=1)
ServicesTextInFormSet = inlineformset_factory(Services, ServicesText, fields=('services',), extra=1)
ServicesImageInFormSet = inlineformset_factory(Services, ServicesImage, fields=('img_s',), extra=1)

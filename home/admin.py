from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Home)
admin.site.register(About)
admin.site.register(Competency)
admin.site.register(Contact)


class PortfolioTechInline(admin.TabularInline):
    model = PortfolioTech
    formset = PortfolioTechFormSet
    extra = 1


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImages
    formset = PortfolioImageFormSet
    extra = 1


class ServicesInline(admin.TabularInline):
    model = ServicesText
    formset = ServicesTextInFormSet
    extra = 1


class ServicesImgInline(admin.TabularInline):
    model = ServicesImage
    formset = ServicesImageInFormSet
    extra = 1


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioTechInline, PortfolioImageInline]


@admin.register(Services)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [ServicesInline, ServicesImgInline]

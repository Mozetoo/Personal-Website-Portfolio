from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/<int:pk>', views.portfolio, name='portfolio'),
    path('services/<int:pk>', views.service, name='services'),

]

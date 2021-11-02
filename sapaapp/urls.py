from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('enquiry', views.enquiry, name='enquiry'),
    path('products', views.products, name='products'),
    path('about', views.about, name='about'),
    path('product/<int:sno>', views.product, name='product'),
]

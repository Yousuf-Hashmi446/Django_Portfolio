from django.urls import path
from .views import index, contact
from main import views

urlpatterns = [
    path('', index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('submit-contact-form/', views.submit_contact_form, name='submit_contact_form'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('contact/', views.contact, name='contact'),
    path("conditions-utilisation/", views.cgu_view, name="cgu"),
    path("politique_confidentialite/", views.cgu_view, name="politique_confidentialite"),
]

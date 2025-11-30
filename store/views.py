from django.shortcuts import render
from adminpanel.models import Slider
from django.utils.translation import get_language

def home(request):
    lang = get_language()[:2]  # 'fr', 'en', 'ar'
    sliders = Slider.objects.filter(is_active=True).order_by('order')
    return render(request, 'store/home.html', {
        'sliders': sliders,
        'lang': lang
    })

# Page des livres
def books(request):
    # Ici tu peux ajouter la logique pour récupérer les livres depuis la base de données
    return render(request, 'store/books.html')

# Page contact
def contact(request):
    return render(request, 'store/contact.html')

def cgu_view(request):
    return render(request, "store/cgu.html")

def politique_confidentialite(request):
    return render(request, "store/politique_confidentialite.html")
    
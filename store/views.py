from django.shortcuts import render

def home(request):
    return render(request, 'store/home.html')

# Page des livres
def books(request):
    # Ici tu peux ajouter la logique pour récupérer les livres depuis la base de données
    return render(request, 'store/books.html')

# Page contact
def contact(request):
    return render(request, 'store/contact.html')

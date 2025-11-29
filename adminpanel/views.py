from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.utils.translation import gettext as _


# Classe pour gérer le login
class CustomLoginView(LoginView):
    template_name = 'adminpanel/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('adminpanel:dashboard')


# Fonction logout
def logout_view(request):
    logout(request)
    return redirect('adminpanel:login')


# Vue du dashboard (protégée par login_required)
@login_required(login_url=reverse_lazy('adminpanel:login'))
def dashboard_view(request):
    # exemples de statistiques à afficher
    stats = {
        'users_count': 123,
        'posts_count': 45,
        'revenue': '10,200 MAD'
    }
    return render(request, 'adminpanel/dashboard.html', {'stats': stats})

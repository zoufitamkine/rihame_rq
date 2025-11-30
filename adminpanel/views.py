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


from django.shortcuts import render, redirect, get_object_or_404
from .models import Slider
from .forms import SliderForm

def slider_list(request):
    sliders = Slider.objects.all().order_by('order')
    return render(request, "adminpanel/sliders/slider_list.html", {"sliders": sliders})

def slider_add(request):
    form = SliderForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("adminpanel:slider_list")
    return render(request, "adminpanel/sliders/slider_form.html", {"form": form})

def slider_edit(request, pk):
    slider = get_object_or_404(Slider, pk=pk)
    form = SliderForm(request.POST or None, request.FILES or None, instance=slider)
    if form.is_valid():
        form.save()
        return redirect("adminpanel:slider_list")
    return render(request, "adminpanel/sliders/slider_form.html", {"form": form, "slider": slider})

def slider_delete(request, pk):
    slider = get_object_or_404(Slider, pk=pk)
    slider.delete()
    return redirect("adminpanel:slider_list")

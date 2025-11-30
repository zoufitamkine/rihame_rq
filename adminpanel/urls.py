from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'adminpanel'


urlpatterns = [
path('login/', views.CustomLoginView.as_view(), name='login'),
path('logout/', views.logout_view, name='logout'),
path('', views.dashboard_view, name='dashboard'),


path("sliders/", views.slider_list, name="slider_list"),
path("sliders/add/", views.slider_add, name="slider_add"),
path("sliders/<int:pk>/edit/", views.slider_edit, name="slider_edit"),
path("sliders/<int:pk>/delete/", views.slider_delete, name="slider_delete"),

# password reset (Django builtins with custom templates)
path('password_reset/', auth_views.PasswordResetView.as_view(
template_name='adminpanel/password_reset_form.html'
), name='password_reset'),
path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
template_name='adminpanel/password_reset_done.html'
), name='password_reset_done'),
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
template_name='adminpanel/password_reset_confirm.html'
), name='password_reset_confirm'),
path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
template_name='adminpanel/password_reset_complete.html'
), name='password_reset_complete'),
]
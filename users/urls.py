from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.views.generic.base import TemplateView
from .backends.activation.views import RegistrationView, ActivationView
from .views import patient_profile
from .forms import RegistrationForm

urlpatterns = [
    # Two-step activation Registration workflow
    path(r'register/', RegistrationView.as_view(form_class=RegistrationForm), name='django_registration_register'),
    path(r'register/complete/', TemplateView.as_view(template_name="django_registration/registration_complete.html"), name="django_registration_complete"),
    path(r'register/closed/', TemplateView.as_view(template_name="django_registration/registration_closed.html"), name="django_registration_disallowed"),
    path(r'activate/complete/', TemplateView.as_view(template_name="django_registration/activation_complete.html"),
         name="django_registration_activation_complete"),
    path(r'activate/<str:activation_key>/', ActivationView.as_view(), name="django_registration_activate"),

    # Patient Profile
    path(r'P_profile/', patient_profile, name='profile'),
    # Medical Doctor Profile
    # path('profile/', profile, name='profile'),
    path(r'login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # Password Reset Views
    path(r'password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path(r'password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path(r'password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path(r'password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
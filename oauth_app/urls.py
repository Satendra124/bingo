from oauth_app.views import start_page
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', start_page),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    
]
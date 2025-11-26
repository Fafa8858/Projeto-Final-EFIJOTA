from django.urls import path
from . import views

urlpatterns = [
    path('cupons/', views.cupons, name='cupons'),
]

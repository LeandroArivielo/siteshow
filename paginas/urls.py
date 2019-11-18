from django.urls import path
from .views import TrabalhoPageView
urlpatterns = [
    path('trabalho', TrabalhoPageView.as_view(), name='trabalho'),
]
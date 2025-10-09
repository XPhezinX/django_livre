from django.urls import path
from recipes.views import home, sobre, contato


urlpatterns = [
    path('', home),  # PATH significa "caminho" e vc adiciona uma rota
    path('sobre/', sobre),
    path('contato/', contato),
]
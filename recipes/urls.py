from django.urls import path
from recipes.views import home


urlpatterns = [
    path('', home),  # PATH significa "caminho" e vc adiciona uma rota
]
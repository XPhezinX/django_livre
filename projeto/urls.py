"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]


#===RECAPTULANDO OS PASSOS===

# 1 - Importa o from "django.http import HttpResponse", que é a request e a resposta do server
# 2 - cria umna função e o que ela vai retornar
# 3 - no "path" vc adiciona como vai ser a URL e oque ela vai apresentar (no caso, a função criada)
# 4 - crie um app e coloque a função lá

# 6 - crie uma pasta de urls no arquivo do app
# 7 - coloque todas as urls lá
# 8 - adicione o include na url do projeto 
# 9 - coloque o caminho de lá dentro do include
# 10 -
# 11 -
# 12 -
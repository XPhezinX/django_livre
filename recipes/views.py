from django.shortcuts import render


# ========== HTTP Request (requisição do site) ==========

# 1 passo:
# def ***(request):  # cria uma função pro seu path
    # return HTTP Response(resposta do servidor)

# 2 passo:
    #return render(request, 'home.html')  #vai retornar o uma renderização de um aquivo html
    #nao esqueça de adiconar seu app nas settings

def home(request): 
   return render (request, 'recipes/pages/home.html')
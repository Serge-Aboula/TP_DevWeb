from datetime import datetime
from django.shortcuts import redirect, render

from Trombinoscoop.forms import LoginForm

def welcome(request):
    return render(request, 'welcome.html',
                  {'current_date_time': datetime.now})

def login(request):
    if not request.POST:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
    form = LoginForm(request.POST)
    
    if not form.is_valid():
        return render(request, 'login.html', {'form': form})
    
    return redirect('/welcome')
    
    
# def login(request):
#     # Teste si le formulaire a été envoyé
#     if not request.POST:
#         # Le formulaire n'a pas été envoyé
#         return render(request, 'login.html')
    
#     # Teste si les paramètres attendus ont été transmis
#     if 'email' not in request.POST or 'password' not in request.POST:
#         error = "Veuillez entrer un email et un mot de passe."
#         return render(request, 'login.html', {'error': error})
    
#     email = request.POST['email']
#     password = request.POST['password']
    
#     #Teste si le mot de passe est le bon
#     if password != '1' or email != 'a@b.c':
#        error = "Email ou mot de passe invalide"
#        return render(request, 'login.html', {'error': error}) 
    
#     # Tout est bon on va à la page d'accueil
#     return redirect('/welcome')

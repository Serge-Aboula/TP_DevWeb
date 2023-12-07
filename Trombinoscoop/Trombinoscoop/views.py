from datetime import datetime
from django.shortcuts import redirect, render
from Trombinoscoop.Trombinoscoop.models import Person

from Trombinoscoop.forms import LoginForm, StudentProfileForm, EmployeeProfileForm

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
    
    user_email = form.cleaned_data['email']
    logged_user = Person.Objects.get(email=user_email)
    request.session['logged_user_id'] = logged_user.id
    
    return redirect('/welcome')

def register(request):
    if not request.GET or  not 'profileType' in request.GET:
        studentForm = StudentProfileForm(prefix='st')
        employeeForm = EmployeeProfileForm(prefix='em')
        return render(request, 'user_profile.html', {'studentForm': studentForm,
                                                     'employeeForm': employeeForm})
    
    studentForm = StudentProfileForm(prefix='st')
    employeeForm = EmployeeProfileForm(prefix='em')
    
    if request.GET['profileType'] == 'student':
        studentForm = StudentProfileForm(request.GET, prefix='st')
    
        if not studentForm.is_valid():
            return render(request, 'user_profile.html', {'studentForm': studentForm,
                                                         'employeeForm': employeeForm})
        
        studentForm.save()
        return redirect('/login')
    
    elif request.GET['profileType'] == 'employee':
        employeeForm = EmployeeProfileForm(request.GET, prefix='em')
    
        if not employeeForm.is_valid():
            return render(request, 'user_profile.html', {'employeeForm': employeeForm,
                                                         'studentForm': studentForm})
        
        employeeForm.save()
        return redirect('/login')
    
    
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

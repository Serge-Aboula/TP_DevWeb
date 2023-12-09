from django import forms
from Trombinoscoop.models import Person, Student, Employee 

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        
        if email and password:
            person = Person.objects.filter(password=password, email=email)
            if not person:
                raise forms.ValidationError("Email ou mot de passe invalide.")
        
        return cleaned_data

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('friends',)

class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ('friends',)
        
class addFriendForm(forms.Form):
    email = forms.EmailField(label='Email')
    
    def clean(self):
        cleaned_data = super(addFriendForm, self).clean()
        email = cleaned_data.get("email")
        
        # Vérifie que le champ est valide
        if email:
            person = Person.objects.filter(email=email)
            if not person:
                raise forms.ValidationError("Email invalide.")
        
        return cleaned_data
 
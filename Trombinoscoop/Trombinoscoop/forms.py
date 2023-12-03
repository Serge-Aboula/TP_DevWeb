from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        
        if email and password:
            if email != 'a@b.ga' and password != '1':
                raise forms.ValidationError("Email ou mot de passe invalide.")
        
        return cleaned_data



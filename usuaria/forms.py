from allauth.account.forms import SignupForm, LoginForm
from django import forms
from django.contrib.auth.hashers import make_password

 
# class CustomSignupForm(forms.Form):
#     print('i got here')
#     fullname = forms.CharField(required=True, label='Fullname')
#     email= forms.EmailField(max_length=50, required=True)
#     password1 = forms.CharField(max_length=32, widget=forms.PasswordInput)
#     password2 = forms.CharField(max_length=32, widget=forms.PasswordInput)

#     def save(self, request):
#         print('here o')
#         fullname = self.cleaned_data['fullname']
#         email = self.cleaned_data['email']
#         password1 = self.cleaned['password1']
#         password2 = self.cleaned_data['password2']
#         print('to be here',self.cleaned_data['fullname'])

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["email"].widget = forms.TextInput(attrs={'placeholder': ''})
        self.fields["password1"].widget = forms.PasswordInput(attrs={'placeholder': ''})
        self.fields["password2"].widget = forms.PasswordInput(attrs={'placeholder': ''})
        
        
    fullname = forms.CharField(required=True, label='Fullname')
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.fullname = self.cleaned_data['fullname']
        user.email = self.cleaned_data['email']
        user.password = make_password(self.cleaned_data['password1'])
        user.save()
        return user

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["login"].widget = forms.TextInput(attrs={'placeholder': ''})
        self.fields["password"].widget = forms.PasswordInput(attrs={'placeholder': ''})
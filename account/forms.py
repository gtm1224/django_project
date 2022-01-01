from django import forms
from django.contrib.auth.models import User
from  .models import UserProfile,UserInfo
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2= forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd ['password2']:
            raise forms.ValidationError('Password do not math.')
        return cd['password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("company","profession","aboutme","photo")
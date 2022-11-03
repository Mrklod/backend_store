from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')

    # def __int__(self,*args,**kwargs):
    #     super(UserLoginForm,self).__init__(*args,**kwargs)
    #     for field_name , field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control py-4'




class UserRegistationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4','placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4','placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4','placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4','placeholder': 'Введите адрес электонной почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4','placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4','placeholder': 'Повторите пароль'}))
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')

    # def __int__(self,*args,**kwargs):
    #     super(UserRegistationForm,self).__init__(*args,**kwargs)
    #     for field_name , field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control py-4'
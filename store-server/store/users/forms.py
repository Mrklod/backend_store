from django.contrib.auth.forms import AuthenticationForm
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

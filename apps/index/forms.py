from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Book


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def save(self, commit=True):
        instance = super(UserForm, self).save(commit=False) # 
        password = self.cleaned_data['password']
        if commit:
            instance.set_password(password)
            instance.save()
        return instance


class LoginAuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': ("Por favor, introduzca un nombre de usuario y contraseña correctos."),
        'inactive': ("Esta cuenta está inactiva."),
    }


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'image', 'description')
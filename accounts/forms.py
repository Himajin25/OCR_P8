""" Update of the built-in forms to point to CustomUser instead of User """
from django.contrib.auth import get_user_model # references AUTH_USER_MODEL in settings.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)

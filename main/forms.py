from django.forms import ModelForm
from users.models import CustomUser

class LoginForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
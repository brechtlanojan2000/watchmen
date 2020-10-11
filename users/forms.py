from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'gender',
            'status',
            'date_of_birth',
            'address',
            'city',
            'state',
            'country',
            'email',
            'phone',
        )

class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'gender',
            'status',
            'date_of_birth',
            'address',
            'city',
            'state',
            'country',
            'email',
            'phone',
        )
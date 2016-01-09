from sundayfunday.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)

from django.forms import ModelForm

class RegisterUserForm(ModelForm):
    class Meta:
        model = User

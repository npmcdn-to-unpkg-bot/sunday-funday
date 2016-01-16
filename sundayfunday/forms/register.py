from sundayfunday.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'preference')

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

from sundayfunday.models import Event
from django.forms import ModelForm
from django import forms

class AddEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'preference', 'owner')

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget = forms.HiddenInput()
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

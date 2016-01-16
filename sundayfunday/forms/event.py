from django.forms import ModelForm
from django import forms

from sundayfunday.models import Event
from sundayfunday.models import Preference

class AddEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'preference', 'owner')

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['owner'].widget = forms.HiddenInput()
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class FilterEventForm(ModelForm):
    class Meta:
        model = Preference
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

from django import forms
from django.core import validators
from ModelTemplatesApp.models import User


class FormName(forms.Form):
    name=forms.CharField()
    email= forms.EmailField()
    verify_email = forms.EmailField(label='Enter your Email again')
    text = forms.CharField(widget=forms.Textarea)

    #CLEAN ALL THE DATA
    def clean(self):
        all_clean_data = super().clean()
        email= all_clean_data['email']
        vmail= all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH")

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'

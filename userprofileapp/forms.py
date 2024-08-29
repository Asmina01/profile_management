

from django import forms
from .models import profile,project,Skill


class ProfileForm(forms.ModelForm):

    class Meta:

        model=profile
        fields="__all__"
        exclude = ['user']


        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the  name'}),
            'bio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the  bio'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter the email'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'enter the email'})
        }

class projectform(forms.ModelForm):

    class Meta:
        model=project
        fields = ['project_name','link', 'description', 'image']



class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'percentage']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Skill Name'}),
            'percentage': forms.NumberInput(attrs={'min': 0, 'max': 100}),
        }




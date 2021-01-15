from django import forms

from mini.models import Profile


class Profileforms(forms.ModelForm):
    
    class Meta:
      
        model = Profile()
        fields = '__all__'
        

from dataclasses import field

from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm#it is a
#build in module inherits form modelform
from django.forms import ModelForm,ImageField,FileInput
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    profile_picture = ImageField(
        required=False,
        error_messages={"invalid": ("Image files only")},
        widget=FileInput,
       )
    class Meta:
        model=User
        
        fields=['username','email','password1','password2']
    def __init__(self,*args,**kwargs):
        super(UserRegisterForm,self).__init__(*args,**kwargs)
        del self.fields['profile_picture']



class UserProfileForm(ModelForm):
   profile_picture = ImageField(
        required=False,
        error_messages={"invalid": ("Image files only")},
        widget=FileInput,
       )
   class Meta:
        model=UserProfile
        fields=['profile_picture']
   def __init__(self,*args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'

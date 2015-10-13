"""
Definition of forms.
"""

from django import forms
#from .models import Student
#from .models import Address
#from .models import Phone
#from .models import Religions
#from .models import StudentLegal
#from .models import StudentPolicy
#from .models import StudentRace
#from .models import StudentUndergraduateInstitution
#from .models import StudentUploads

class PageOneForm(forms.Form): 
    email = forms.CharField(label='Email', required=True)
    first_name = forms.CharField(label='First Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
     

#from django.contrib.auth.forms import AuthenticationForm
#from django.utils.translation import ugettext_lazy as _

#class BootstrapAuthenticationForm(AuthenticationForm):
#    """Authentication form which uses boostrap CSS."""
#    username = forms.CharField(max_length=254,
#                               widget=forms.TextInput({
#                                   'class': 'form-control',
#                                   'placeholder': 'User name'}))
#    password = forms.CharField(label=_("Password"),
#                               widget=forms.PasswordInput({
#                                   'class': 'form-control',
#                                   'placeholder':'Password'}))
#
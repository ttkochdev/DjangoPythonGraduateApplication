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
    middle_name = forms.CharField(label='Middle Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    suffix_name = forms.CharField(label='Suffix', required=True)
    preferred_first_name = forms.CharField(label='Prefered First Name', required=True)
    birth_last_name = forms.CharField(label='Birth Last Name', required=True)
    country = forms.BooleanField()
    address1 = forms.CharField(label='Mailing Address', required=True) 
    address2 = forms.CharField(label='Mailing Address 2', required=True)
    city = forms.CharField(label='City', required=True)
    state = forms.CharField(label='State', required=True)
    zipcode = forms.CharField(label='Zip Code', required=True)
    international_phone = forms.BooleanField()
    permanent_phone = forms.CharField(label='Permanent Telephone Number', required=True)
    GENDER_TYPE_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        )
    gender = forms.ChoiceField(choices=GENDER_TYPE_CHOICES)
    birth_date = forms.DateTimeField(input_formats='%m/%d/%Y')
    birth_place = forms.CharField()
    ETHNICITY_TYPE_CHOICES = (
        ('YES','Yes, Hispanic or Latino'),
        ('NO','No, not Hispanic or Latino'),
        )
    gender = forms.ChoiceField(choices=ETHNICITY_TYPE_CHOICES)
    RACE_CHOICES = (
        ('American_Indian','American Indian or Alaska Native'),
        ('Asian','Asian'),
        ('Black','Black or African American'),
        ('Native_Hawaiian','Native Hawaiian or Other Pacific Islander'),
        ('White','White'),
        )
    race = forms.MultipleChoiceField(choices=RACE_CHOICES,widget=forms.CheckboxSelectMultiple())
    denomination = forms.ChoiceField(choices=(('db','Database'),('val','Values')))
    is_citizen = forms.ChoiceField(choices=(('yes','Yes'),('legal','Legal Permanent Resident'),('no','No')))

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
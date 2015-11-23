"""
Definition of forms.
"""

from django import forms

from graduate.models import Race
from graduate.models import Religions
from graduate.models import Majors
from graduate.models import StudentRace
from graduate.models import Influences

from localflavor.us.us_states import STATE_CHOICES
from django_countries import countries
from django_countries.fields import CountryField
from django_countries.fields import LazyTypedChoiceField
from django_countries.widgets import CountrySelectWidget
from captcha.fields import CaptchaField
from localflavor.us.forms import USSocialSecurityNumberField
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from datetime import date, datetime

from functools import partial
DateInput = partial(forms.DateInput, {'class': 'birthdatepicker'})

class PageOneForm(forms.Form): 

    def __init__(self, *args, **kwargs):
        self.raceinit = kwargs.pop('raceinit')
        super(PageOneForm, self).__init__(*args, **kwargs)        
        if 'initial' not in kwargs:
            kwargs['initial'] = {}
        self.initial['race']=self.raceinit

    email = forms.CharField(label='Email', required=True) #Student
    first_name = forms.CharField(label='First Name', required=True)#Student
    middle_name = forms.CharField(label='Middle Name')#Student
    last_name = forms.CharField(label='Last Name', required=True)    #Student
    social_security = USSocialSecurityNumberField(required=False)#Student
    SUFFIX_TYPE_CHOICES = (
        ('',''),
        ('Jr','Jr.'),
        ('Sr','Sr.'),
        ('II','II'),
        ('III','III'),
        ('IV','IV'),
        )
    suffix = forms.ChoiceField(choices=SUFFIX_TYPE_CHOICES, required=False)#Student
    preferred_first_name = forms.CharField(label='Prefered First Name', required=False)#Student
    birth_last_name = forms.CharField(label='Birth Last Name', required=True)#Student
    GENDER_TYPE_CHOICES = (
        ('',''),
        ('M','Male'),
        ('F','Female'),
        )
    gender = forms.ChoiceField(choices=GENDER_TYPE_CHOICES, required=False) #Student
    birth_date = forms.DateField(widget=DateInput(), required=False) #Student
    birth_place = forms.CharField(label='Birthplace', required=False) #Student
    ETHNICITY_TYPE_CHOICES = (
        ('',''),
        ('YES','Yes, Hispanic or Latino'),
        ('NO','No, not Hispanic or Latino'),
        ) 
    ethnicity = forms.ChoiceField(choices=ETHNICITY_TYPE_CHOICES, required=False) #Student            
    denomination = forms.ModelChoiceField(queryset=Religions.objects.all(), required=False)#Student
    is_citizen = forms.ChoiceField(choices=(("",""),('yes','Yes'),('legal','Legal Permanent Resident'),('no','No')), required=False)#Student
    internationalcheck = forms.BooleanField(required=False)
    COUNTRY_CHOICES = tuple(countries)
    COUNTRY_CHOICES = (('', ''),) + COUNTRY_CHOICES
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False)#address Address    
    citizenship_country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False) #citizen questions #Address
    residence_country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False) #Address   
    alien_reg_no = forms.CharField(label='Alien Registration Number', required=False) 
    address1 = forms.CharField(label='Mailing Address', required=True) #Address
    address2 = forms.CharField(label='Mailing Address 2', required=False) #Address
    city = forms.CharField(label='City', required=True)#Address
    STATE_CHOICES = (('', ''),) + STATE_CHOICES
    state = forms.ChoiceField(choices=STATE_CHOICES, required=True)#Address   
    zipcode = forms.CharField(label='Zip Code', required=True)#Address
    international_phonecheck = forms.BooleanField(required=False)
    IS_INTERNATIONAL_STUDENT_CHOICES = (
        ('',''),
        ('YES','Yes'),
        ('NO','No'),
        ) 
    is_international_student = forms.ChoiceField(choices=IS_INTERNATIONAL_STUDENT_CHOICES, required=False) #Student     
    ALIEN_STATUS_CHOICES = (
        ('',''),
        ('F1 Student','F1 Student'),
        ('F2','F2'),
        ('H1','H1'),
        ('H4','H4'),
        ('J1 Exchange Visitor','J1 Exchange Visitor'),
        ('K1','K1'),
        ('PR Permanent Resident US','PR Permanent Resident US'),
        ('TD','TD'),
        ('Unknown','Unknown'),
        ) 
    alien_status = forms.ChoiceField(choices=ALIEN_STATUS_CHOICES, required=False) #Student 
    permanent_phone = forms.CharField(label='Permanent Telephone Number', required=False) #Phone
    cell_phone = forms.CharField(label='Cell Phone Number', required=False) #Phone   
    race = forms.ModelMultipleChoiceField(queryset=Race.objects.all(),widget=forms.CheckboxSelectMultiple(), required=False) #StudentRace
    

class Institutions(forms.Form):
    undergraduate_institution = forms.CharField(required=True)
    ceeb = forms.CharField(required=True)

class PageTwoForm(forms.Form):
    
    def season():
        doy = datetime.today().timetuple().tm_yday
        currentYear = date.today().year

        # "day of year" ranges for the northern hemisphere
        spring = range(80, 172)
        summer = range(172, 264)
        fall = range(264, 355)
        if doy in spring:
            season = 'spring'
            seasonChoices = ( ('summer', 'Summer (June) ' + str(currentYear) ), ('fall', 'Fall (September) '+ str(currentYear) ), ('winter', 'Winter (January) '+ str(currentYear + 1)), ('spring', 'Spring (March) '+ str(currentYear + 1)) )
        elif doy in summer:
            season = 'summer'
            seasonChoices = ( ('fall', 'Fall (September) '+ str(currentYear)), ('winter', 'Winter (January) '+ str(currentYear + 1)), ('spring', 'Spring (March) '+ str(currentYear + 1)), ('summer', 'Summer (June) '+ str(currentYear + 1)) )
        elif doy in fall:
            season = 'fall'
            seasonChoices = ( ('winter', 'Winter (January) '+ str(currentYear + 1)), ('spring', 'Spring (March) '+ str(currentYear + 1)), ('summer', 'Summmer (June) '+ str(currentYear + 1)), ('fall', 'Fall (September) '+ str(currentYear + 1)) )
        else:
            season = 'winter'
            seasonChoices = ( ('spring', 'Spring (March) '+ str(currentYear)), ('summer', 'Summer (June) '+ str(currentYear)), ('fall', 'Fall (September) '+ str(currentYear)), ('winter', 'Winter (January) '+ str(currentYear + 1)) )
        return seasonChoices
    
    seasons = season()    
    START_TERM_CHOICES = (('', ''),) + seasons
    start_term = forms.ChoiceField(choices=START_TERM_CHOICES ,label='When do you intend to enroll at North Central College?') 
    student_load_intent = forms.ChoiceField(label='What is your intended course load?', choices=(('',''), ('fulltime','Full-time'),('parttime','Part-time')), required=False)   
    planned_major = forms.ModelChoiceField(queryset=Majors.objects.all(), label='What is your program of study?', required=False)        
    refered_by_name = forms.CharField(label='Friend / Relative Name', required=False)
    refered_by_relationship = forms.CharField(label='Relationship To You', required=False)
    refered_by_name2 = forms.CharField(label='Friend / Relative Name', required=False)
    refered_by_relationship2 = forms.CharField(label='Relationship To You', required=False)
    influence = forms.ModelChoiceField(queryset=Influences.objects.all(), label='Who or what helped influence your decision to apply to North Central College?', required=False) 
    POLICY_CHOICES=(
        ('1','Yes'),
        ('0','No'),)
    policy = forms.ChoiceField(choices=POLICY_CHOICES, label='Have you ever been accused or charged with violating a code of student conduct or institutional policy, or been suspended, placed on probation, dismissed, or expelled from any high school or college?', widget=forms.RadioSelect(), initial=0)
    policy_reason = forms.CharField(label='If yes, please explain why you were suspended/dismissed in 140 characters or less.', required=False)
    LEGAL_CHOICES=(
        ('1','Yes'),
        ('0','No'),)
    legal = forms.ChoiceField(choices=LEGAL_CHOICES, label='Have you ever been arrested, indicted, or convicted of anything other than a minor traffic violation?', widget=forms.RadioSelect(), initial=0)
    legal_reason = forms.CharField(label='If yes, please explain your conviction in 140 characters or less.', required=False)
    employer = forms.CharField(label='Employer Name', required=False)
    outside_us_employment = forms.BooleanField(label='Employment address outside of the United States?',required=False)
    COUNTRY_CHOICES = tuple(countries)
    COUNTRY_CHOICES = (('', ''),) + COUNTRY_CHOICES
    employer_country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False) 
    employment_address = forms.CharField(required=False)
    employment_address_outside_us = forms.BooleanField(required=False)
    employment_city = forms.CharField(required=False)
    STATE_CHOICES = (('', ''),) + STATE_CHOICES
    employment_state = forms.ChoiceField(choices=STATE_CHOICES, required=False)
    employment_zip = forms.CharField(required=False)
    tuition_remission = forms.BooleanField(required=False)
    gi = forms.BooleanField(required=False)
    captcha = CaptchaField()



class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

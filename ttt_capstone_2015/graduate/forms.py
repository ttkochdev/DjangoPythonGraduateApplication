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
#from localflavor.us.forms import USStateSelect
from django_countries import countries
from django_countries.fields import CountryField
from django_countries.fields import LazyTypedChoiceField
from django_countries.widgets import CountrySelectWidget

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
        #print("\n\npage1form\n\n")
        if 'initial' not in kwargs:
            kwargs['initial'] = {}
            #print('set kwargs')
        #else:
            #print("fromdb")
            #print([c.raceid for c in StudentRace.objects.filter(student_id='1')])
            #print("\n\nfromself.raceinit\n")
            #print(self.raceinit)
        #print(self.fields['race'])
        #print("\n\n")
        self.initial['race']=self.raceinit
        #self.fields['race'].initial = ['1','2','3']#self.raceinit
        #print(self.fields['race'].initial)
#        self.fields['race'].initial = [c.pk for c in StudentRace.object.filter()]
        #if(StudentRace.objects.filter(student_id='1').exists()):

            #self.fields['race'].initial = [c.raceid for c in StudentRace.objects.filter(student_id='1')]

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
    ##INSERT INTO `admissions.dev.capstone`.`graduate_religions` (`rid`, `name`) VALUES (NULL, 'No Respons, required=Truee'), (NULL, 'African Methodist Episcopal'), (NULL, 'Assembly of God'), (NULL, 'Baptist'), (NULL, 'Bible Church'), (NULL, 'Buddhist'), (NULL, 'Calvary Christian'), (NULL, 'Christian'), (NULL, 'Christian Orthodox'), (NULL, 'Church of Brethren'), (NULL, 'Church of Christ'), (NULL, 'Church of Christian Science'), (NULL, 'Church of God'), (NULL, 'Community'), (NULL, 'Congregational'), (NULL, 'Disciples of Christ'), (NULL, 'Episcopal'), (NULL, 'Evangelical'), (NULL, 'Evangelical Lutheran'), (NULL, 'Greek Orthodox'), (NULL, 'Hindu'), (NULL, 'Independent'), (NULL, 'Islam/Moslem'), (NULL, 'Jewish'), (NULL, 'Lutheran-Missouri'), (NULL, 'Lutheran-Other'), (NULL, 'Mennonite'), (NULL, 'Mormon'), (NULL, 'No Church Affiliation'), (NULL, 'Non-Affiliated Christian'), (NULL, 'Non-Christian'), (NULL, 'Non-Denominational'), (NULL, 'Other'), (NULL, 'Other Protestant'), (NULL, 'Pentecostal'), (NULL, 'Presbyterian'), (NULL, 'Reformed'), (NULL, 'Roman Catholic'), (NULL, 'Serbian Orthodox'), (NULL, 'Seventh Day Adventist'), (NULL, 'Unitarian/Universalist'), (NULL, 'United Church of Christ'), (NULL, 'United Methodist'), (NULL, 'United Presbyterian'), (NULL, 'Wesleyan');
    denomination = forms.ModelChoiceField(queryset=Religions.objects.all(), required=False)#Student
    is_citizen = forms.ChoiceField(choices=(("",""),('yes','Yes'),('legal','Legal Permanent Resident'),('no','No')), required=False)#Student
    internationalcheck = forms.BooleanField(required=False)

    COUNTRY_CHOICES = tuple(countries)
    COUNTRY_CHOICES = (('', ''),) + COUNTRY_CHOICES
    country = forms.ChoiceField(choices=COUNTRY_CHOICES)#address Address    
    citizenship_country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False) #citizen questions #Address
    residence_country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False) #Address   
    alien_reg_no = forms.CharField(label='Alien Registration Number', required=False) 
    address1 = forms.CharField(label='Mailing Address', required=True) #Address
    address2 = forms.CharField(label='Mailing Address 2', required=False) #Address
    city = forms.CharField(label='City', required=True)#Address
    STATE_CHOICES = (('', ''),) + STATE_CHOICES
    state = forms.ChoiceField(choices=STATE_CHOICES, required=True)#Address
    #state = forms.CharField(label='State', required=True)
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
    
    #INSERT INTO `admissions.dev.capstone`.`graduate_race` (`rid`, `race`) VALUES (NULL, 'American Indian or Alaska Native'), (NULL, 'Asian'), (NULL, 'Black or African American'), (NULL, 'Native Hawaiian or Other Pacific Islander'), (NULL, 'White');
    race = forms.ModelMultipleChoiceField(queryset=Race.objects.all(),widget=forms.CheckboxSelectMultiple(), required=False) #StudentRace
    

class Institutions(forms.Form):
    undergraduate_institution = forms.CharField()
    ceeb = forms.CharField()
    #extra_field_count = forms.CharField(widget=forms.HiddenInput())

    #def __init__(self, *args, **kwargs):
    #    extra_fields = kwargs.pop('extra', 0)
    #    print('\nextra_fields\n')
    #    print(extra_fields)

    #    super(PageTwoForm, self).__init__(*args, **kwargs)
    #    self.fields['extra_field_count'].initial = extra_fields

    #    for index in range(int(extra_fields)):
    #        # generate extra fields in the number specified via extra_fields
    #        self.fields['extra_field_{index}'.format(index=index)] = forms.CharField()

class PageTwoForm(forms.Form):
    
    def season():
        doy = datetime.today().timetuple().tm_yday
        currentYear = date.today().year

        # "day of year" ranges for the northern hemisphere
        spring = range(80, 172)
        summer = range(172, 264)
        fall = range(264, 355)
        # winter = everything else
    
        #(("",""),("",""),...)
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
    #INSERT INTO `admissions.dev.capstone`.`graduate_majors` (`mid`, `majors`) VALUES (NULL, 'Master of Arts in Education: Curriculum and Instruction'), (NULL, 'Master of Arts in Education:  Educational Leadership & Administration'), (NULL, 'Master of Arts in Liberal Studies:  Culture and Society'), (NULL, 'Master of Arts in Liberal Studies:  Writing, Editing, and Publishing'), (NULL, 'Master of Business Administration:  Accounting'), (NULL, 'Master of Business Administration:  Change Management'), (NULL, 'Master of Business Administration:  Finance'), (NULL, 'Master of Business Administration:  Human Resource Management'), (NULL, 'Master of Business Administration:  Management'), (NULL, 'Master of Business Administration:  Marketing'), (NULL, 'Master of International Business Administration'), (NULL, 'Master of Leadership Studies:  Professional Leadership'), (NULL, 'Master of Leadership Studies:  Higher Education'), (NULL, 'Master of Leadership Studies:  Social Entrepreneurship'), (NULL, 'Master of Leadership Studies: Sport Leadership'), (NULL, 'Master of Science in Web and Internet Applications');
    planned_major = forms.ModelChoiceField(queryset=Majors.objects.all(), label='What is your program of study?', required=False)        

    refered_by_name = forms.CharField(label='Friend / Relative Name', required=False)
    refered_by_relationship = forms.CharField(label='Relationship To You', required=False)
    refered_by_name2 = forms.CharField(label='Friend / Relative Name', required=False)
    refered_by_relationship2 = forms.CharField(label='Relationship To You', required=False)
    influence = forms.ModelChoiceField(queryset=Influences.objects.all(), label='Who or what helped influence your decision to apply to North Central College?', required=False) 
    POLICY_CHOICES=(
        ('Yes','Yes'),
        ('No','No'),)
    policy = forms.ChoiceField(choices=POLICY_CHOICES, label='Have you ever been accused or charged with violating a code of student conduct or institutional policy, or been suspended, placed on probation, dismissed, or expelled from any high school or college?', widget=forms.RadioSelect())
    policy_reason = forms.CharField(label='If yes, please explain why you were suspended/dismissed in 140 characters or less.', required=False)
    LEGAL_CHOICES=(
        ('Yes','Yes'),
        ('No','No'),)
    legal = forms.ChoiceField(choices=LEGAL_CHOICES, label='Have you ever been arrested, indicted, or convicted of anything other than a minor traffic violation?', widget=forms.RadioSelect())
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

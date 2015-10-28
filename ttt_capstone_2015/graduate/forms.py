"""
Definition of forms.
"""

from django import forms
#from django.forms.models import model_to_dict
from graduate.models import Race

class PageOneForm(forms.Form): 
    email = forms.CharField(label='Email', required=True)
    first_name = forms.CharField(label='First Name', required=True)
    middle_name = forms.CharField(label='Middle Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)    
    SUFFIX_TYPE_CHOICES = (
        ('Jr','Jr.'),
        ('Sr','Sr.'),
        ('II','II'),
        ('III','III'),
        ('IV','IV'),
        )
    suffix = forms.ChoiceField(choices=SUFFIX_TYPE_CHOICES)
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
    international_phone = forms.CharField(label='International Telephone Number', required=True)
    GENDER_TYPE_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        )
    gender = forms.ChoiceField(choices=GENDER_TYPE_CHOICES)
    birth_date = forms.DateTimeField(input_formats='%m/%d/%Y')
    birth_place = forms.CharField(label='Birthplace', required=True)
    ETHNICITY_TYPE_CHOICES = (
        ('YES','Yes, Hispanic or Latino'),
        ('NO','No, not Hispanic or Latino'),
        ) 
    gender = forms.ChoiceField(choices=ETHNICITY_TYPE_CHOICES)
     #INSERT INTO `admissions.dev.capstone`.`graduate_race` (`rid`, `race`) VALUES (NULL, 'American Indian or Alaska Native'), (NULL, 'Asian'), (NULL, 'Black or African American'), (NULL, 'Native Hawaiian or Other Pacific Islander'), (NULL, 'White');
    #RACE_CHOICES = (
    #    ('American_Indian','American Indian or Alaska Native'),
    #    ('Asian','Asian'),
    #    ('Black','Black or African American'),
    #    ('Native_Hawaiian','Native Hawaiian or Other Pacific Islander'),
    #    ('White','White'),
    #    )
    #race = forms.MultipleChoiceField(choices=RACE_CHOICES,widget=forms.CheckboxSelectMultiple())
    #racedata = model_to_dict(Race.objects.all())
    #race = forms.MultipleChoiceField(choices=racedata,widget=forms.CheckboxSelectMultiple())
    race = forms.ModelMultipleChoiceField(queryset=Race.objects.values('race'),widget=forms.CheckboxSelectMultiple())
    denomination = forms.ChoiceField(choices=(('db','Database'),('val','Values')))
    is_citizen = forms.ChoiceField(choices=(('yes','Yes'),('legal','Legal Permanent Resident'),('no','No')))

class PageTwoForm(forms.Form):

    START_TERM_CHOICES = (
        #dynamic
        )
    start_term = forms.CharField(label='When do you intend to enroll at North Central College?') #make dynamic ChoiceField
    student_load_intent = forms.ChoiceField(label='What is your intended course load?', choices=(('fulltime','Full-time'),('parttime','Part-time')))
    planned_major = forms.CharField(label='What is your program of study?')
    undergraduate_institution = forms.CharField()
    ceeb = forms.CharField()
    refered_by_name = forms.CharField(label='Friend / Relative Name')
    refered_by_relationship = forms.CharField(label='Relationship To You')
    refered_by_name2 = forms.CharField(label='Friend / Relative Name')
    refered_by_relationship2 = forms.CharField(label='Relationship To You')
    influence = forms.CharField(label='Who or what helped influence your decision to apply to North Central College?') 
    policy = forms.BooleanField(label='Have you ever been accused or charged with violating a code of student conduct or institutional policy, or been suspended, placed on probation, dismissed, or expelled from any high school or college?')
    policy_reason = forms.CharField(label='If yes, please explain why you were suspended/dismissed in 140 characters or less.')
    legal = forms.BooleanField(label='Have you ever been arrested, indicted, or convicted of anything other than a minor traffic violation?')
    legal_reason = forms.CharField(label='If yes, please explain your conviction in 140 characters or less.')
    employer = forms.CharField(label='Employer Name')
    outside_us_employment = forms.BooleanField(label='Employment address outside of the United States?')
    employment_city = forms.CharField()
    employment_state = forms.CharField() #dropdown of states....
    employment_zip = forms.CharField()
    tuition_remission = forms.BooleanField()
    gi = forms.BooleanField()


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
from django.db import models


from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from crypto import * #https://djangosnippets.org/snippets/824/
#from Crypto.Cipher import Blowfish
from django.conf import settings
import binascii

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Phone(models.Model):    
    phone = models.CharField(max_length=75)
    typeflag = models.CharField(max_length=255)

    def __str__(self):              
        return "%s %s" % (self.phone, self.typeflag)

class Student(AbstractBaseUser): #models.Model
    id = models.AutoField(primary_key=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth'] #YYYY-MM-DD

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    batch_id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    suffix_name = models.CharField(max_length=30)
    preferred_first_name = models.CharField(max_length=30)
    birth_last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=45)
    birth_place = models.CharField(max_length=255)
    #birth_date = models.DateTimeField(auto_now=False, auto_now_add=False) #may have to come back to this one after testing....there are known issues with django datetime
    ethnicity = models.CharField(max_length=255)
    is_citizen = models.IntegerField(default=0)
    social_security_number = models.CharField(max_length=32) #this was not syncing with the db like the others...need to check funcitonality carefully. 

    def _get_ssn(self):
        enc_obj = Blowfish.new( settings.SECRET_KEY )
        return u"%s" % enc_obj.decrypt( binascii.a2b_hex(self.social_security_number) ).rstrip()

    def _set_ssn(self, ssn_value):
        enc_obj = Blowfish.new( settings.SECRET_KEY )
        repeat = 8 - (len( ssn_value ) % 8)
        ssn_value = ssn_value + " " * repeat
        self.social_security_number = binascii.b2a_hex(enc_obj.encrypt( ssn_value ))

    ssn = property(_get_ssn, _set_ssn)
    denomination = models.IntegerField(default=0)
    start_term = models.CharField(max_length=255)
    student_load_intent = models.CharField(max_length=255)
    residency_status = models.CharField(max_length=255)
    planned_major = models.CharField(max_length=255)
    level = models.CharField(max_length=3)    
    refered_by_name = models.CharField(max_length=255)
    refered_by_relationship = models.CharField(max_length=255)
    refered_by_name2 = models.CharField(max_length=255)
    refered_by_relationship2 = models.CharField(max_length=255)
    influence = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    tution_remission = models.IntegerField(default=0)
    gi = models.IntegerField(default=0)
    phone = models.ManyToManyField(Phone)

    def __str__(self):
        return self.email

class Address(models.Model):
    said = models.AutoField(primary_key=True)
    sid = models.ForeignKey(Student)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=32)
    country = models.CharField(max_length=255)
    typeflag = models.CharField(max_length=255) #'Flag for Student, Employer'

    def __str__(self):
        return self.said


class Religions(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class StudentLegal(models.Model):
    slid = models.AutoField(primary_key=True)
    sid = models.ForeignKey(Student)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return self.sid

class StudentPolicy(models.Model):
    spid = models.AutoField(primary_key=True)
    sid = models.ForeignKey(Student)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return self.sid

class StudentRace(models.Model):
    srid = models.AutoField(primary_key=True)
    sid = models.ForeignKey(Student)
    race = models.CharField(max_length=255)

    def __str__(self):
        return self.srid

    #maybe try making this a model form? 
class StudentUndergraduateInstitution(models.Model):
    soiid = models.AutoField(primary_key=True)
    sid = models.ForeignKey(Student)
    name = models.CharField(max_length=255)
    ceeb = models.CharField(max_length=10)

    def __str__(self):
        return self.soiid

class StudentUploads(models.Model):
    uid = models.AutoField(primary_key=True)
    sid = models.ForeignKey(Student)
    name = models.CharField(max_length=255)

    _data = models.TextField(
            db_column='data',
            blank=True)

    def set_data(self, data):
        self._data = base64.encodestring(data)

    def get_data(self):
        return base64.decodestring(self._data)

    data = property(get_data, set_data)

    def __str__(self):
        return self.uid        

class Race(models.Model):
    rid = models.AutoField(primary_key=True)
    race = models.CharField(max_length=255)
    
    def __str__(self):
        return self.race

class Majors(models.Model):
    mid = models.AutoField(primary_key=True)
    majors = models.CharField(max_length=255)
    
    def __str__(self):
        return self.majors



##DB inserts

### delete database and recreate empty in order to syncdb()
### yes to create damin = ttkoch@noctrl.edu - 1989-12-05 - password
### 
###

##race
#INSERT INTO `admissions.dev.capstone`.`graduate_race` (`rid`, `race`) VALUES (NULL, 'American Indian or Alaska Native'), (NULL, 'Asian'), (NULL, 'Black or African American'), (NULL, 'Native Hawaiian or Other Pacific Islander'), (NULL, 'White');
##religions
#INSERT INTO `admissions.dev.capstone`.`graduate_religions` (`rid`, `name`) VALUES (NULL, 'No Response'), (NULL, 'African Methodist Episcopal'), (NULL, 'Assembly of God'), (NULL, 'Baptist'), (NULL, 'Bible Church'), (NULL, 'Buddhist'), (NULL, 'Calvary Christian'), (NULL, 'Christian'), (NULL, 'Christian Orthodox'), (NULL, 'Church of Brethren'), (NULL, 'Church of Christ'), (NULL, 'Church of Christian Science'), (NULL, 'Church of God'), (NULL, 'Community'), (NULL, 'Congregational'), (NULL, 'Disciples of Christ'), (NULL, 'Episcopal'), (NULL, 'Evangelical'), (NULL, 'Evangelical Lutheran'), (NULL, 'Greek Orthodox'), (NULL, 'Hindu'), (NULL, 'Independent'), (NULL, 'Islam/Moslem'), (NULL, 'Jewish'), (NULL, 'Lutheran-Missouri'), (NULL, 'Lutheran-Other'), (NULL, 'Mennonite'), (NULL, 'Mormon'), (NULL, 'No Church Affiliation'), (NULL, 'Non-Affiliated Christian'), (NULL, 'Non-Christian'), (NULL, 'Non-Denominational'), (NULL, 'Other'), (NULL, 'Other Protestant'), (NULL, 'Pentecostal'), (NULL, 'Presbyterian'), (NULL, 'Reformed'), (NULL, 'Roman Catholic'), (NULL, 'Serbian Orthodox'), (NULL, 'Seventh Day Adventist'), (NULL, 'Unitarian/Universalist'), (NULL, 'United Church of Christ'), (NULL, 'United Methodist'), (NULL, 'United Presbyterian'), (NULL, 'Wesleyan');
##majors
#INSERT INTO `admissions.dev.capstone`.`graduate_majors` (`mid`, `majors`) VALUES (NULL, 'Master of Arts in Education: Curriculum and Instruction'), (NULL, 'Master of Arts in Education:  Educational Leadership & Administration'), (NULL, 'Master of Arts in Liberal Studies:  Culture and Society'), (NULL, 'Master of Arts in Liberal Studies:  Writing, Editing, and Publishing'), (NULL, 'Master of Business Administration:  Accounting'), (NULL, 'Master of Business Administration:  Change Management'), (NULL, 'Master of Business Administration:  Finance'), (NULL, 'Master of Business Administration:  Human Resource Management'), (NULL, 'Master of Business Administration:  Management'), (NULL, 'Master of Business Administration:  Marketing'), (NULL, 'Master of International Business Administration'), (NULL, 'Master of Leadership Studies:  Professional Leadership'), (NULL, 'Master of Leadership Studies:  Higher Education'), (NULL, 'Master of Leadership Studies:  Social Entrepreneurship'), (NULL, 'Master of Leadership Studies: Sport Leadership'), (NULL, 'Master of Science in Web and Internet Applications');






#class MyUser(AbstractBaseUser):
#    email = models.EmailField(
#        verbose_name='email address',
#        max_length=255,
#        unique=True,
#    )
#    date_of_birth = models.DateField()
#    is_active = models.BooleanField(default=True)
#    is_admin = models.BooleanField(default=False)

#    objects = MyUserManager()

#    USERNAME_FIELD = 'email'
#    REQUIRED_FIELDS = ['date_of_birth'] #YYYY-MM-DD

#    def get_full_name(self):
#        # The user is identified by their email address
#        return self.email

#    def get_short_name(self):
#        # The user is identified by their email address
#        return self.email

#    def __str__(self):              # __unicode__ on Python 2
#        return self.email

#    def has_perm(self, perm, obj=None):
#        "Does the user have a specific permission?"
#        # Simplest possible answer: Yes, always
#        return True

#    def has_module_perms(self, app_label):
#        "Does the user have permissions to view the app `app_label`?"
#        # Simplest possible answer: Yes, always
#        return True

    #@property
    #def is_staff(self):
    #    "Is the user a member of staff?"
    #    # Simplest possible answer: All admins are staff
    #    return self.is_admin
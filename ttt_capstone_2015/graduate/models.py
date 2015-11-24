from django.db import models


from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


#from simplecrypt import encrypt, decrypt
from fernet_fields import EncryptedTextField
from django.conf import settings
import binascii

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            #date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            #date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Student(AbstractBaseUser): #models.Model
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['email'] #YYYY-MM-DD

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
    batch_id = models.IntegerField(null=True)
    first_name = models.CharField(max_length=30, null=True)
    middle_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    suffix = models.CharField(max_length=30, null=True)
    preferred_first_name = models.CharField(max_length=30, null=True)
    birth_last_name = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=45, null=True)
    birth_place = models.CharField(max_length=255, null=True)
    ethnicity = models.CharField(max_length=255, null=True)
    is_citizen = models.CharField(max_length=3, null=True)
    social_security = EncryptedTextField(null=True)
    denomination = models.IntegerField(null=True)
    start_term = models.CharField(max_length=255, null=True)
    student_load_intent = models.CharField(max_length=255, null=True)
    residency_status = models.CharField(max_length=255, null=True)
    planned_major = models.CharField(max_length=255, null=True)
    #level = models.CharField(max_length=3)    
    refered_by_name = models.CharField(max_length=255, null=True)
    refered_by_relationship = models.CharField(max_length=255, null=True)
    refered_by_name2 = models.CharField(max_length=255, null=True)
    refered_by_relationship2 = models.CharField(max_length=255, null=True)
    influence = models.CharField(max_length=255, null=True)
    employer = models.CharField(max_length=255, null=True)
    tuition_remission = models.NullBooleanField()    
    gi = models.NullBooleanField()
    citizenship_country = models.CharField(max_length=60, null=True)
    residence_country = models.CharField(max_length=60, null=True)
    alien_reg_no = models.CharField(max_length=15, null=True)
    is_international_student = models.CharField(max_length=3, null=True) 
    alien_status = models.CharField(max_length=30, null=True)
    employment_address_outside_us = models.BooleanField(default=0)
    submitted = models.IntegerField(default=0)
    internationalcheck = models.NullBooleanField()

    def __str__(self):
        return self.email

#would need to maintain hidden previously enter phone fields in order to do this, because of the updating problem. 
class Phone(models.Model):    
    student = models.ForeignKey(Student)
    phone = models.CharField(max_length=75, null=True)
    typeflag = models.CharField(max_length=255)

    def __str__(self):              
        return "%s %s" % (self.phone, self.typeflag)

class Address(models.Model):
    student = models.ForeignKey(Student)
    address1 = models.CharField(max_length=255, null=True)
    address2 = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    zipcode = models.CharField(max_length=32, null=True)
    country = models.CharField(max_length=255, null=True)
    typeflag = models.CharField(max_length=255) #'Flag for Student, Employer'

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.address1, self.address2, self.city, self.state, self.zipcode, self.country, self.typeflag)


class Religions(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class StudentLegal(models.Model):
    student = models.OneToOneField(Student, primary_key=True)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return self.reason

class StudentPolicy(models.Model):
    student = models.OneToOneField(Student, primary_key=True)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return self.student

class StudentRace(models.Model):
    student = models.ForeignKey(Student)
    raceid = models.CharField(max_length=255)

    def __str__(self):
        return self.raceid

    #maybe try making this a model form? 
class StudentUndergraduateInstitution(models.Model):
    student = models.ForeignKey(Student)
    name = models.CharField(max_length=255, null=True)
    ceeb = models.CharField(max_length=10, null=True)

    def __str__(self):
        return "%s %s" % (self.name, self.ceeb)

#class StudentUploads(models.Model):
#    ceeb = models.ForeignKey(Student)
#    name = models.CharField(max_length=255)

#    _data = models.TextField(
#            db_column='data',
#            blank=True)

#    def set_data(self, data):
#        self._data = base64.encodestring(data)

#    def get_data(self):
#        return base64.decodestring(self._data)

#    data = property(get_data, set_data)

#    def __str__(self):
#        return self.name        

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

class Influences(models.Model):
    influence = models.CharField(max_length=255)
    
    def __str__(self):
        return self.influence

##DB inserts

### delete database and recreate empty in order to syncdb()
### yes to create damin = ttkoch@noctrl.edu - 1989-12-05 - password
### 
###
#pbkdf2_sha256$20000$gufZNBMAOxYp$fvYOSRqVLtMF1sK6hSaaXXDSrcsjvJ/gQFrQPIWIcu8=
#INSERT INTO `admissions.dev.capstone`.`graduate_race` (`rid`, `race`) VALUES (NULL, 'American Indian or Alaska Native'), (NULL, 'Asian'), (NULL, 'Black or African American'), (NULL, 'Native Hawaiian or Other Pacific Islander'), (NULL, 'White');
#INSERT INTO `admissions.dev.capstone`.`graduate_religions` (`rid`, `name`) VALUES (NULL, 'No Response'), (NULL, 'African Methodist Episcopal'), (NULL, 'Assembly of God'), (NULL, 'Baptist'), (NULL, 'Bible Church'), (NULL, 'Buddhist'), (NULL, 'Calvary Christian'), (NULL, 'Christian'), (NULL, 'Christian Orthodox'), (NULL, 'Church of Brethren'), (NULL, 'Church of Christ'), (NULL, 'Church of Christian Science'), (NULL, 'Church of God'), (NULL, 'Community'), (NULL, 'Congregational'), (NULL, 'Disciples of Christ'), (NULL, 'Episcopal'), (NULL, 'Evangelical'), (NULL, 'Evangelical Lutheran'), (NULL, 'Greek Orthodox'), (NULL, 'Hindu'), (NULL, 'Independent'), (NULL, 'Islam/Moslem'), (NULL, 'Jewish'), (NULL, 'Lutheran-Missouri'), (NULL, 'Lutheran-Other'), (NULL, 'Mennonite'), (NULL, 'Mormon'), (NULL, 'No Church Affiliation'), (NULL, 'Non-Affiliated Christian'), (NULL, 'Non-Christian'), (NULL, 'Non-Denominational'), (NULL, 'Other'), (NULL, 'Other Protestant'), (NULL, 'Pentecostal'), (NULL, 'Presbyterian'), (NULL, 'Reformed'), (NULL, 'Roman Catholic'), (NULL, 'Serbian Orthodox'), (NULL, 'Seventh Day Adventist'), (NULL, 'Unitarian/Universalist'), (NULL, 'United Church of Christ'), (NULL, 'United Methodist'), (NULL, 'United Presbyterian'), (NULL, 'Wesleyan');
#INSERT INTO `admissions.dev.capstone`.`graduate_majors` (`mid`, `majors`) VALUES (NULL, 'Master of Arts in Education: Curriculum and Instruction'), (NULL, 'Master of Arts in Education:  Educational Leadership & Administration'), (NULL, 'Master of Arts in Liberal Studies:  Culture and Society'), (NULL, 'Master of Arts in Liberal Studies:  Writing, Editing, and Publishing'), (NULL, 'Master of Business Administration:  Accounting'), (NULL, 'Master of Business Administration:  Change Management'), (NULL, 'Master of Business Administration:  Finance'), (NULL, 'Master of Business Administration:  Human Resource Management'), (NULL, 'Master of Business Administration:  Management'), (NULL, 'Master of Business Administration:  Marketing'), (NULL, 'Master of International Business Administration'), (NULL, 'Master of Leadership Studies:  Professional Leadership'), (NULL, 'Master of Leadership Studies:  Higher Education'), (NULL, 'Master of Leadership Studies:  Social Entrepreneurship'), (NULL, 'Master of Leadership Studies: Sport Leadership'), (NULL, 'Master of Science in Web and Internet Applications');
#INSERT INTO `admissions.dev.capstone`.`graduate_studentrace` (`id`, `student_id`, `raceid`) VALUES (NULL, '1', '2'), (NULL, '1', '5');
#INSERT INTO `admissions.dev.capstone`.`graduate_influences` (`id`, `influence`) VALUES (NULL, 'Academic Programs'), (NULL, 'Athletic Programs'), (NULL, 'Attended NCC Summer Camp'), (NULL, 'Campus Tour'), (NULL, 'Campus Visit'), (NULL, 'Class Size Small'), (NULL, 'College Fair'), (NULL, 'Extracurricular Opportunities'), (NULL, 'Financial Aid'), (NULL, 'Friend(s)'), (NULL, 'High School Coach'), (NULL, 'High School Counselor'), (NULL, 'High School Teacher'), (NULL, 'Internet Site'), (NULL, 'Location'), (NULL, 'Mailings'), (NULL, 'North Central Alum'), (NULL, 'North Central Coach'), (NULL, 'North Central Counselor'), (NULL, 'North Central Faculty'), (NULL, 'North Central Student'), (NULL, 'Open House'), (NULL, 'Other'), (NULL, 'Publications'), (NULL, 'Relative'), (NULL, 'Reputation'), (NULL, 'Size of School'), (NULL, 'United Methodist Affiliate'), (NULL, 'Video');

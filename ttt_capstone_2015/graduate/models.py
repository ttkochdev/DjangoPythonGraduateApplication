﻿from django.db import models


from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from crypto import * #https://djangosnippets.org/snippets/824/
#from Crypto.Cipher import Blowfish
from django.conf import settings
import binascii

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    batch_id = models.IntegerField(10)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    suffix_name = models.CharField(max_length=30)
    preferred_first_name = models.CharField(max_length=30)
    birth_last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=45)
    birth_place = models.CharField(max_length=255)
    birth_date = models.DateTimeField(auto_now=False, auto_now_add=False) #may have to come back to this one after testing....there are known issues with django datetime
    ethnicity = models.CharField(max_length=255)
    is_citizen = models.IntegerField(1)
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
    denomination = models.IntegerField(3)
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
    tution_remission = models.IntegerField(1)
    gi = models.IntegerField(1)

    def __str__(self):
        return self.id

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

class Phone(models.Model):
    spid = models.AutoField(primary_key=True) 
    sid = models.ForeignKey(Student)
    phone = models.CharField(max_length=75)
    typeflag = models.CharField(max_length=255)

    def __str__(self):
        return self.spid

class Religions(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.rid

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


class MyUser(AbstractBaseUser):
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
    REQUIRED_FIELDS = ['date_of_birth']

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

    #@property
    #def is_staff(self):
    #    "Is the user a member of staff?"
    #    # Simplest possible answer: All admins are staff
    #    return self.is_admin
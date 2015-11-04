﻿from .models import *

class saveForms(object):
    """description of class"""


    def savePage1(data):
        print(data)
        #data.iterlists()      

        #get values from page1 form in session variable
        first_name = data.get("first_name", "")
        middle_name = data.get("middle_name", "")
        last_name = data.get("last_name", "")
        social_security = data.get("social_security", "")
        suffix = data.get("suffix", "")
        preferred_first_name = data.get("preferred_first_name", "")
        birth_last_name = data.get("birth_last_name", "")
        #internationalcheck
        country = data.get("country", "")
        citizenship_country = data.get("citizenship_country", "")
        residence_country = data.get("residence_country", "")
        address1 = data.get("address1", "")
        address2 = data.get("address2", "")
        city = data.get("city", "")
        state = data.get("state", "")
        zipcode = data.get("zipcode", "")
        #international_phonecheck = data.get("international_phonecheck", "")
        permanent_phone = data.get("permanent_phone", "")
        international_phone = data.get("international_phone", "")
        gender = data.get("gender", "")
        date_of_birth = data.get("date_of_birth", "")
        ethnicity = data.get("ethnicity", "")
        race = data.get("race", "")
        denomination = data.get("denomination", "")
        is_citizen = data.get("is_citizen", "")

        
        #Student.objects.create(batch_id="123", first_name="first", last_name="last", date_of_birth=dob, is_citizen="1", denomination="1", level="1", tution_remission="1", gi="1")
    
        obj, created = Student.objects.update_or_create(email="ttkoch@noctrl.edu", 
                                                        defaults={'batch_id':'0','first_name': first_name, 'middle_name':'middle_name', 'last_name':last_name,
                                                                  'social_security':'','suffix':'','preferred_first_name':'',
                                                                  'birth_last_name':'','country':'','residence_country':'',
                                                                  'address1':'','address2':'','city':'',
                                                                  'state':'','zipcode':'','permanent_phone':'',
                                                                  'international_phone':'','gender':'','date_of_birth':date_of_birth,
                                                                  'ethnicity':'','race':'','denomination':'0','is_citizen':'0',
                                                                  'level':'1', 'tution_remission':'1', 'gi':'1',
                                                                  })
        #def updatePage1(data):    

    #def savePage2(data):
    #def updatePage2(data):

    #def savePage3(data):
from .models import *

class saveForms(object):
    """description of class"""


    def savePage1(data):
        print(data)
        #data.iterlists()      

        #get values from page1 form in session variable
        email = data.get("email", "")
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
        international_phonecheck = data.get("international_phonecheck", "")
        permanent_phone = data.get("permanent_phone", "")
        cell_phone = data.get("cell_phone", "")
        gender = data.get("gender", "")
        birth_date = data.get("birth_date", "")
        ethnicity = data.get("ethnicity", "")
        race = data.get("race", "")
        denomination = data.get("denomination", "")
        is_citizen = data.get("is_citizen", "")


        #Student.objects.create(batch_id="123", first_name="first", last_name="last", date_of_birth=dob, is_citizen="1", denomination="1", level="1", tution_remission="1", gi="1")
        #if international_phonecheck == 1:
        
        #need to get the correct primary key for the phone
        #permphone = Phone.objects.update_or_create(pk=1, defaults={'phone':permanent_phone, 'typeflag':'permanent_phone'})[0]
        #permphone.save()
        #else:
        #cellphone = Phone.objects.update_or_create(pk=2, defaults={'phone':cell_phone, 'typeflag':'permanent_phone'})[0]
        #cellphone.save()

        studentobj, created = Student.objects.update_or_create(email=email, 
                                                        defaults={'first_name': first_name, 'middle_name':middle_name, 'last_name':last_name,
                                                                  'social_security':social_security,'suffix':suffix,'preferred_first_name':preferred_first_name,
                                                                  'birth_last_name':birth_last_name,'gender':gender,'date_of_birth':birth_date,
                                                                  'ethnicity':ethnicity,'denomination':denomination,'is_citizen':is_citizen,
                                                                  'permanent_phone':permanent_phone, 'cell_phone':cell_phone,                                                                  
                                                                  })
        #studentobj = Student(first_name = first_name, middle_name = middle_name, 
        #                     last_name = last_name, social_security = '', suffix = '', preferred_first_name = '', 
        #                     birth_last_name = '', gender = '', 
        #                     date_of_birth = birth_date, ethnicity = '',  denomination = '0', 
        #                     is_citizen = is_citizen, level = '1', )
        #studentobj.save()
        

        #if Student.objects.filter(email=email).exists():
        #    phonepk = Phone.objects.get(student_id=studentres.id, type=permanent_phone)
        
        #if Student.objects.filter(email=email).exists():
        #    studentres = Student.objects.get(email=email)
        #    studentphones = Phone.objects.filter(student_id=studentres.id)
        #    for s in studentphones:
        #        phoneres = Phone.objects.get(pk=s.id)
        #        phoneres.student = studentres  
        #        phoneres.save()

            #studentres = Student.objects.get(email=email)
            #if Phone.objects.filter(student_id=studentres.id).filter(phone=permanent_phone).exists(): #.filter(phone=permanent_phone)
            #    #update permanent phone
            #    phoneres = Phone.objects.get(student_id=studentres.id, phone=permanent_phone)
            #    phoneres.student = studentres  
            #    phoneres.save()
            #if Phone.objects.filter(student_id=studentres.id).filter(phone=cell_phone).exists():
            #    #update cell
            #    phoneres = Phone.objects.get(student_id=studentres.id, phone=cell_phone)
            #    phoneres.student = studentres  
            #    phoneres.save()

            #if Phone.objects.exclude(student_id=studentres.id, phone=permanent_phone).exists():
            #    #create permanent phone entry
            #    if permanent_phone:
            #        permanent_phoneobj = Phone(phone=permanent_phone, typeflag = international_phonecheck, student = studentres)
            #        permanent_phoneobj.save()
            #if Phone.objects.exclude(student_id=studentres.id, phone=cell_phone).exists():
            #    if cell_phone:
            #        cell_phoneobj = Phone(phone=cell_phone, typeflag = international_phonecheck, student = studentres)
            #        cell_phoneobj.save()    

        #if Student.objects.get(email=email).exists():
        #    studentres = Student.objects.get(email=email)
        #    if Phone.objects.get(student=studentres.id).exists():
        #        phoneres = Phone.objects.get(student=studentres.id)
        #    else:
        #        phoneres = Phone.objects.create(phone)
        #phoneres.student = studentres        

        
        #phoneobj = Phone(phone='test', typeflag ='type', student = studentobj)
        #phoneobj.save()

        #country = '', residence_country = '', address1 = '', address2 = '', city = '', state = '',  zipcode = '',
        #race = '',
        #tution_remission = '1', gi = '1', batch_id = '0', 

        #obj.phone.add(permphone, cellphone)        
        #def updatePage1(data):    

    #def savePage2(data):
    #def updatePage2(data):

    #def savePage3(data):
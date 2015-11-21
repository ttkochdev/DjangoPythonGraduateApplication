from .models import *

class getForms(object):
    """description of class"""


    def getPage1(student_session_id):
        #print(data) 

        #get values from page1 form in session variable
        #email = data.get("email")
        #first_name = data.get("first_name", "")
        #middle_name = data.get("middle_name", None)
        #last_name = data.get("last_name", "")
        #social_security = data.get("social_security", "")
        #suffix = data.get("suffix", None)
        #preferred_first_name = data.get("preferred_first_name", None)
        #birth_last_name = data.get("birth_last_name", None)        
        #country = data.get("country", None)        
        #address1 = data.get("address1", None)
        #address2 = data.get("address2", None)
        #city = data.get("city", None)
        #state = data.get("state", None)
        #zipcode = data.get("zipcode", None)
        #international_phonecheck = data.get("international_phonecheck", None)
        #permanent_phone = data.get("permanent_phone", None)
        #cell_phone = data.get("cell_phone", None)
        #gender = data.get("gender", None)
        #birth_date = data.get("birth_date", None) or None
        #birth_place = data.get("birth_place", None)
        #ethnicity = data.get("ethnicity", None)
        ##race = data.getList("race", None)
        #denomination = data.get("denomination", None)
        #try:
        #    denomination = int(denomination)
        #except ValueError:
        #    denomination = None
        #is_citizen = data.get("is_citizen", None)
        #citizenship_country = data.get("citizenship_country", None)
        #residence_country = data.get("residence_country", None)
        #alien_reg_no = data.get("alien_reg_no", None)
        #is_international_student = data.get("is_international_student", None)
        #alient_status = data.get("alient_status", None)
        print("\n\n\nGET FORMS PAGE-1\n\n\n")
        student = Student.objects.get(pk=student_session_id)
        #sid = student.id 
        #results = Student.objects.filter(phone__student=student)
        #print(results)
        print("\n\naddress")
        saddress = Address.objects.get(student=student, typeflag="student")
        #address = Address.objects.get(student=student, typeflag="employer")
        print(saddress)
        print("\n\nphone")
        cphone= Phone.objects.get(student=student, typeflag="cell_phone")
        pphone= Phone.objects.get(student=student, typeflag="permanent_phone")
        print(cphone)

        print("\n\nGET DATA\n\n")
        data = {'state': saddress.state, 'email': student.email, 'is_citizen': student.is_citizen, 'alien_reg_no': student.alien_reg_no, 
         'is_international_student': student.is_international_student, #'csrfmiddlewaretoken': 'otwFahh2kZjDjbDOCl7UZ0HWzZLJlgyH',
         'denomination': student.denomination, 'address2': saddress.address2, 'gender': student.gender, 'birth_date': student.date_of_birth,
         'cell_phone': cphone.phone, 'birth_last_name': student.birth_last_name, 'zipcode': saddress.zipcode, #'race': race,
         'alien_status': student.alien_status, 'country': saddress.country, 'last_name': student.last_name, 'residence_country': student.residence_country,
         'first_name': student.first_name, 'city': saddress.city, 'address1': saddress.address1, 'ethnicity': student.ethnicity,
         'birth_place': student.birth_place, 'middle_name': student.middle_name, 'social_security': student.social_security,
         'citizenship_country': student.citizenship_country, 'permanent_phone': pphone.phone, 'suffix': student.suffix, 'preferred_first_name': student.preferred_first_name}
        print(data)
        print("\n\n")
        return data
        #raceinit = 


    #    #save student
    #    studentobj_uc, created = Student.objects.update_or_create(email=email, 
    #                                                    defaults={'first_name': first_name, 'middle_name':middle_name, 'last_name':last_name,
    #                                                              'social_security': social_security,'suffix':suffix,'preferred_first_name':preferred_first_name,
    #                                                              'birth_last_name':birth_last_name,'gender':gender,'date_of_birth':birth_date, 'birth_place':birth_place,
    #                                                              'ethnicity':ethnicity,'denomination':denomination,'is_citizen':is_citizen, 'citizenship_country':citizenship_country, 'residence_country':residence_country,
    #                                                              'alien_reg_no': alien_reg_no,'is_international_student': is_international_student,'alient_status': alient_status,                                                                 
    #                                                              })
    #    #update or create (studentobj_uc) would return NO object if nothing was updated or created. 
    #    if Student.objects.filter(email=email).exists():
    #         studentobj = Student.objects.get(email=email)
    #    #if there is a student then you can update and create fields attached to student
    #    if studentobj:  
            
    #        #save phone         
    #        permanentphone, permpcreated = Phone.objects.update_or_create(student=studentobj, typeflag="permanent_phone", 
    #                                                    defaults={'phone':permanent_phone, 'typeflag':'permanent_phone', 'student':studentobj})
    #        cellphone, cellpcreated = Phone.objects.update_or_create(student=studentobj, typeflag="cell_phone", 
    #                                                    defaults={'phone':cell_phone, 'typeflag':'cell_phone', 'student':studentobj})

    #        #save address
    #        #generate defaults dynamically to remove US info for foreign country and vice versa
    #        address, addresscreated = Address.objects.update_or_create(student=studentobj, typeflag="student", 
    #                                                    defaults={'address1':address1,'address2':address2,'city':city,'state':state,
    #                                                              'zipcode':zipcode,'country':country, 'typeflag':'student', 'student':studentobj})       

    #        #save race
    #        if StudentRace.objects.filter(student=studentobj).exists():                
    #            studentrace = StudentRace.objects.filter(student=studentobj)
    #            studentrace.delete()
    #        if raceinit:
    #            for race in raceinit:
    #                sr = StudentRace(student=studentobj, raceid=race)
    #                sr.save()


    ##def savePage2(data):

    ##def savePage3(data):
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

        studentobj, created = Student.objects.update_or_create(email=email, 
                                                        defaults={'first_name': first_name, 'middle_name':middle_name, 'last_name':last_name,
                                                                  'social_security': Student._set_ssn(Student,social_security),'suffix':suffix,'preferred_first_name':preferred_first_name,
                                                                  'birth_last_name':birth_last_name,'gender':gender,'date_of_birth':birth_date,
                                                                  'ethnicity':ethnicity,'denomination':denomination,'is_citizen':is_citizen,
                                                                  #'permanent_phone':permanent_phone, 'cell_phone':cell_phone,                                                                  
                                                                  })
        
        if studentobj:  
            #update or create phone         
            permanentphone, permpcreated = Phone.objects.update_or_create(student=studentobj, typeflag="permanent_phone", 
                                                        defaults={'phone':permanent_phone, 'typeflag':'permanent_phone', 'student':studentobj})
            cellphone, cellpcreated = Phone.objects.update_or_create(student=studentobj, typeflag="cell_phone", 
                                                        defaults={'phone':cell_phone, 'typeflag':'cell_phone', 'student':studentobj})

            #update or create address

            #update or create race



            #    permphone = Phone.objects.filter(student_id=studentres.id).get(typeflag="permanent_phone")                                
            #    permphone.student = studentres
            #    permphone.phone = permanent_phone
            #    permphone.typeflag = "permanent_phone"
            #    permphone.save();

            #if Phone.objects.filter(student_id=studentres.id).filter(typeflag="permanent_phone").exists():
            #    permphone = Phone.objects.filter(student_id=studentres.id).get(typeflag="permanent_phone")                                
            #    permphone.student = studentres
            #    permphone.phone = permanent_phone
            #    permphone.typeflag = "permanent_phone"
            #    permphone.save();
            #else:
            #    pp = Phone(phone=permanent_phone, typeflag='permanent_phone', student=studentres)
            #    pp.save()            
            #if Phone.objects.filter(student_id=studentres.id).filter(typeflag="cell_phone").exists():                
            #    cellphone = Phone.objects.filter(student_id=studentres.id).get(typeflag="cell_phone")     
            #    cellphone.student = studentres
            #    cellphone.phone = cell_phone
            #    cellphone.typeflag = "cell_phone"
            #    cellphone.save();
            #else:
            #    cp = Phone(phone=cell_phone, typeflag='cell_phone', student=studentres)
            #    cp.save()
    

             

    #def savePage2(data):

    #def savePage3(data):
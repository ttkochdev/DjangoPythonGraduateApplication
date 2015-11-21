from .models import *

class saveForms(object):
    """description of class"""


    def savePage1(data, raceinit):
        print(data) 

        #get values from page1 form in session variable
        email = data.get("email")
        first_name = data.get("first_name", "")
        middle_name = data.get("middle_name", None)
        last_name = data.get("last_name", "")
        social_security = data.get("social_security", "")
        suffix = data.get("suffix", None)
        preferred_first_name = data.get("preferred_first_name", None)
        birth_last_name = data.get("birth_last_name", None)
        #internationalcheck
        country = data.get("country", None)
        citizenship_country = data.get("citizenship_country", None)
        residence_country = data.get("residence_country", None)
        address1 = data.get("address1", None)
        address2 = data.get("address2", None)
        city = data.get("city", None)
        state = data.get("state", None)
        zipcode = data.get("zipcode", None)
        international_phonecheck = data.get("international_phonecheck", None)
        permanent_phone = data.get("permanent_phone", None)
        cell_phone = data.get("cell_phone", None)
        gender = data.get("gender", None)
        birth_date = data.get("birth_date", None) or None
        ethnicity = data.get("ethnicity", None)
        #race = data.getList("race", None)
        denomination = data.get("denomination", None)
        #print("\n\ndenomination\n")
        #print(denomination)
        try:
            denomination = int(denomination)
        except ValueError:
            denomination = None
        is_citizen = data.get("is_citizen", None)

        studentobj, created = Student.objects.update_or_create(email=email, 
                                                        defaults={'first_name': first_name, 'middle_name':middle_name, 'last_name':last_name,
                                                                  'social_security': social_security,'suffix':suffix,'preferred_first_name':preferred_first_name,
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
            #generate defaults dynamically to remove US info for foreign country and vice versa
            address, addresscreated = Address.objects.update_or_create(student=studentobj, typeflag="student", 
                                                        defaults={'address1':address1,'address2':address2,'city':city,'state':state,
                                                                  'zipcode':zipcode,'country':country, 'typeflag':'student', 'student':studentobj})       
            print('\n\nhere\n\n')     
            #delete all previous for user and create new race additions
            if StudentRace.objects.filter(student=studentobj).exists():
                print('\n\nhere333\n\n')   
                studentrace = StudentRace.objects.filter(student=studentobj)
                studentrace.delete()
                print("\n\nstuff deleted\n\n")
            if raceinit:
                print("if raceinit is true")
                for race in raceinit:
                    sr = StudentRace(student=studentobj, raceid=race)
                    sr.save()


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
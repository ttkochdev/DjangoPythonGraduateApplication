from .models import *

class saveForms(object):
    """description of class"""


    def savePage1(data, raceinit):
        #print(data) 

        #get values from page1 form in session variable
        email = data.get("email")
        first_name = data.get("first_name", "")
        middle_name = data.get("middle_name", None)
        last_name = data.get("last_name", "")
        social_security = data.get("social_security", "")
        suffix = data.get("suffix", None)
        preferred_first_name = data.get("preferred_first_name", None)
        birth_last_name = data.get("birth_last_name", None)        
        country = data.get("country", None)        
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
        birth_place = data.get("birth_place", None)
        ethnicity = data.get("ethnicity", None)
        #race = data.getList("race", None)
        denomination = data.get("denomination", None)
        try:
            denomination = int(denomination)
        except ValueError:
            denomination = None
        is_citizen = data.get("is_citizen", None)
        citizenship_country = data.get("citizenship_country", None)
        residence_country = data.get("residence_country", None)
        alien_reg_no = data.get("alien_reg_no", None)
        is_international_student = data.get("is_international_student", None)
        alient_status = data.get("alient_status", None)

        #save student
        studentobj_uc, created = Student.objects.update_or_create(email=email, 
                                                        defaults={'first_name': first_name, 'middle_name':middle_name, 'last_name':last_name,
                                                                  'social_security': social_security,'suffix':suffix,'preferred_first_name':preferred_first_name,
                                                                  'birth_last_name':birth_last_name,'gender':gender,'date_of_birth':birth_date, 'birth_place':birth_place,
                                                                  'ethnicity':ethnicity,'denomination':denomination,'is_citizen':is_citizen, 'citizenship_country':citizenship_country, 'residence_country':residence_country,
                                                                  'alien_reg_no': alien_reg_no,'is_international_student': is_international_student,'alient_status': alient_status,                                                                 
                                                                  })
        #update or create (studentobj_uc) would return NO object if nothing was updated or created. 
        if Student.objects.filter(email=email).exists():
             studentobj = Student.objects.get(email=email)
        #if there is a student then you can update and create fields attached to student
        if studentobj:  
            
            #save phone         
            permanentphone, permpcreated = Phone.objects.update_or_create(student=studentobj, typeflag="permanent_phone", 
                                                        defaults={'phone':permanent_phone, 'typeflag':'permanent_phone', 'student':studentobj})
            cellphone, cellpcreated = Phone.objects.update_or_create(student=studentobj, typeflag="cell_phone", 
                                                        defaults={'phone':cell_phone, 'typeflag':'cell_phone', 'student':studentobj})

            #save address
            #needs to generate defaults dynamically to remove US info for foreign country and vice versa
            address, addresscreated = Address.objects.update_or_create(student=studentobj, typeflag="student", 
                                                        defaults={'address1':address1,'address2':address2,'city':city,'state':state,
                                                                  'zipcode':zipcode,'country':country, 'typeflag':'student', 'student':studentobj})       

            #save race
            if StudentRace.objects.filter(student=studentobj).exists():                
                studentrace = StudentRace.objects.filter(student=studentobj)
                studentrace.delete()
            if raceinit:
                for race in raceinit:
                    sr = StudentRace(student=studentobj, raceid=race)
                    sr.save()


    def savePage2(email, data, institutions):
        print("\n\ninstitution formset\n",institutions, "\n\n")

        email = email
        start_term = data.get("start_term")
        student_load_intent = data.get("student_load_intent")
        planned_major = data.get("planned_major")        
        tuition_remission = data.get("tuition_remission")          
        if tuition_remission is 'on':
            tuition_remission = 1
        else:
            tuition_remission = 0
        gi = data.get("gi")
        if gi is 'on':
            gi = 1
        else:
            gi = 0
        refered_by_name = data.get("refered_by_name")
        refered_by_name2 = data.get("refered_by_name2")
        refered_by_relationship = data.get("refered_by_relationship")
        refered_by_relationship2 = data.get("refered_by_relationship2")
        influence = data.get("influence")        

        employer = data.get('employer')
        employer_country = data.get("employer_country")
        employment_address = data.get("employment_address")
        employment_zip = data.get("employment_zip")
        employment_city = data.get("employment_city")
        employment_state = data.get("employment_state")
        
        legal_reason = data.get("legal_reason")   
        policy_reason = data.get("policy_reason")  
        

        #institutions-0-undergraduate_institution
        #institutions-0-ceeb
        #institutions-1-undergraduate_institution
        #institutions-1-ceeb


        #save student
        studentobj_uc, created = Student.objects.update_or_create(email=email, 
                                                        defaults={'start_term':start_term, 'student_load_intent':student_load_intent, 'employer':employer,
                                                                  'planned_major': planned_major,'tuition_remission':tuition_remission,'influence':influence,      
                                                                  'gi':gi,'refered_by_name':refered_by_name, 'refered_by_name2':refered_by_name2,
                                                                  'refered_by_relationship':refered_by_relationship,'refered_by_relationship2':refered_by_relationship2,                                              
                                                                  })
           #update or create (studentobj_uc) would return NO object if nothing was updated or created. 
        if Student.objects.filter(email=email).exists():
             studentobj = Student.objects.get(email=email)
        #if there is a student then you can update and create fields attached to student
        if studentobj:  
        #save employer address
            address, addresscreated = Address.objects.update_or_create(student=studentobj, typeflag="employer", 
                                                        defaults={'address1':employment_address,'city':employment_city,'state':employment_state,
                                                                  'zipcode':employment_zip,'country':employer_country, 'typeflag':'employer', 'student':studentobj})       
        #{'institutions-0-undergraduate_institution': 'Wabash College', 'student_load_intent': 'fulltime', 
        # 'save': 'save page', 'employer_country': '', 'tuition_remission': 'on', 
        # 'institutions-MAX_NUM_FORMS': '1000', 'legal': 'Yes', 'employment_zip': '47304',
        # 'gi': 'on', 'policy_reason': '', 'employment_address': 'Employment Mailing Address',
        # 'institutions-TOTAL_FORMS': '2', 'employment_address_outside': '', 'page': 'Page2', 
        # 'refered_by_relationship2': 'Relationship to you ', 'policy': 'No', 'start_term': 'winter',
        # 'institutions-MIN_NUM_FORMS': '0', 'institutions-1-undergraduate_institution': 'North Central College',
        # 'employment_city': 'Muncie', 'institutions-INITIAL_FORMS': '0', 'employer_address_outside_us': '0', 
        # 'baseUrl': '', 'influence': '', 'institutions-0-ceeb': '1895', 'refered_by_name': 'Friend Relative Name',
        # 'employment_state': 'AL', 'csrfmiddlewaretoken': 'sKjvFDV57pwuDe89yEVgy2opEAqBtbjH', 'refered_by_relationship': 'Relationship to you',
        # 'legal_reason': '', 'planned_major': '1', 'institutions-1-ceeb': '1111', 'refered_by_name2': 'Friend Relative Name 2'}
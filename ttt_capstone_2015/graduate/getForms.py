from .models import *

class getForms(object):
    """description of class"""
    def getPage1(student_session_id):
        student = Student.objects.get(pk=student_session_id)
        if Address.objects.filter(student=student, typeflag="student").exists():
            saddress = Address.objects.get(student=student, typeflag="student")
        else:
            saddress = Address()
        if Phone.objects.filter(student=student, typeflag="cell_phone"):
            cphone= Phone.objects.get(student=student, typeflag="cell_phone")
        else:
            cphone = Phone()   
         
        if Phone.objects.filter(student=student, typeflag="permanent_phone"):                
            pphone= Phone.objects.get(student=student, typeflag="permanent_phone")
        else:
            pphone= Phone()
        data = {'state': saddress.state, 'email': student.email, 'is_citizen': student.is_citizen, 'alien_reg_no': student.alien_reg_no, 
         'is_international_student': student.is_international_student, #'csrfmiddlewaretoken': 'otwFahh2kZjDjbDOCl7UZ0HWzZLJlgyH',
         'denomination': student.denomination, 'address2': saddress.address2, 'gender': student.gender, 'birth_date': str(student.date_of_birth),
         'cell_phone': cphone.phone, 'birth_last_name': student.birth_last_name, 'zipcode': saddress.zipcode, #'race': race,
         'alien_status': student.alien_status, 'country': saddress.country, 'last_name': student.last_name, 'residence_country': student.residence_country,
         'first_name': student.first_name, 'city': saddress.city, 'address1': saddress.address1, 'ethnicity': student.ethnicity,
         'birth_place': student.birth_place, 'middle_name': student.middle_name, 'social_security': student.social_security,
         'citizenship_country': student.citizenship_country, 'permanent_phone': pphone.phone, 'suffix': student.suffix, 'preferred_first_name': student.preferred_first_name}
        return data

    def getPage2(student_session_id):
        student = Student.objects.get(pk=student_session_id)
        if Address.objects.filter(student=student, typeflag="employer").exists():
            address = Address.objects.get(student=student, typeflag="employer")
        else:
            address = Address()
        if StudentLegal.objects.filter(student=student).exists():
            legal = StudentLegal.objects.get(student=student)
            legalcheck = 1
        else:
            legal = StudentLegal()
            legalcheck = 0
        if StudentPolicy.objects.filter(student=student).exists():
            policy = StudentPolicy.objects.get(student=student)
            policycheck = 1
        else:
            policy = StudentPolicy()
            policycheck = 0
        print('\nUndergrad Inst\n')
        iTOTAL_FORMS = 1
        extra = {}
        if StudentUndergraduateInstitution.objects.filter(student=student).exists(): 
            ugradinst = StudentUndergraduateInstitution.objects.filter(student=student)
            iTOTAL_FORMS = len(ugradinst)           
            for i, inst in enumerate(ugradinst):
                temp = {'institutions-'+str(i)+'-undergraduate_institution': inst.name,'institutions-'+str(i)+'-ceeb': inst.ceeb}
                extra.update(temp)
        data = {'student_load_intent': student.student_load_intent, 'employer_country': address.country, 'tuition_remission': student.tuition_remission, 
                'legal': legalcheck, 'employment_zip': address.zipcode, 'gi': student.gi, 'policy_reason': policy.reason, 
                'employment_address': address.address1, 'employment_address_outside_us': student.employment_address_outside_us, 
                'refered_by_relationship2': student.refered_by_relationship2, 'policy': policycheck, 'start_term': student.start_term, 
                'employment_city': address.city, 'influence': student.influence, 'employer':student.employer,
                'refered_by_name': student.refered_by_name, 'employment_state': address.state, 'refered_by_relationship': student.refered_by_relationship,
                'legal_reason': legal.reason, 'planned_major': student.planned_major, 'refered_by_name2': student.refered_by_name2,
                #'institutions-0-undergraduate_institution': 'Wabash College', 'institutions-1-undergraduate_institution': 'North Central College',
                #'institutions-0-ceeb': '1895', 'institutions-1-ceeb': '1111',
                'institutions-MAX_NUM_FORMS': '1000','institutions-TOTAL_FORMS': iTOTAL_FORMS, 'institutions-INITIAL_FORMS': '0',
                'institutions-MIN_NUM_FORMS': '0'
                }
        data.update(extra)
        print("\nlogged in data\n")
        print(data)
        #'institutions-0-undergraduate_institution': 'Wabash College', 'institutions-1-undergraduate_institution': 'North Central College', 'institutions-0-ceeb': '1895', 'institutions-1-ceeb': '1111','institutions-MAX_NUM_FORMS': '1000','institutions-TOTAL_FORMS': '2', 'institutions-INITIAL_FORMS': '0','institutions-MIN_NUM_FORMS': '0'
        #'save': 'save page', 'csrfmiddlewaretoken': 'sKjvFDV57pwuDe89yEVgy2opEAqBtbjH', 'page': 'Page2',
        return data
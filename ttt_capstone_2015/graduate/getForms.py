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

from .models import *

class saveForms(object):
    """description of class"""


    def savePage1(data):
        print(data)
        print('haha\n\n\n')
        dob = data.get("date_of_birth", "")
        print(dob)
        Student.objects.create(batch_id="123", first_name="first", last_name="last", date_of_birth=dob, is_citizen="1", denomination="1", level="1", tution_remission="1", gi="1")
    #def updatePage1(data):    

    #def savePage2(data):
    #def updatePage2(data):

    #def savePage3(data):
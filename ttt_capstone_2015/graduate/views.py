﻿"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from datetime import date, datetime
from django.forms import formset_factory
import json
from django.core.mail import send_mail

from .forms import PageOneForm
from .forms import PageTwoForm
from .forms import Institutions

from .saveForms import *

from graduate.models import Race

def page1(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        #print(request.POST,"\n\n")
        form = PageOneForm(request.POST)
        #for key in request.POST:
        #    print (key)
        
        #print(form)
        #save post data to session
        #request.session['form1'] =
        request.session['form_data_page1'] = request.POST
        
        print(request.session["form_data_page1"])
        #if submit = page2 then go to page 2 else if page-3 then go to page 3
        if(request.POST.get('page2', '')):
            return HttpResponseRedirect('/page-2/')
        elif (request.POST.get('page3', '')):
            return HttpResponseRedirect('/page-3/')
        elif (request.POST.get('save', '')):
            saveForms.savePage1(request.session['form_data_page1'])
            return HttpResponseRedirect('/page-1/') 

    # if a GET (or any other method) we'll create a blank form
    else:     
        
        print(request.session.get('form_data_page1'))  
        #check if login session exists
        #if so populate session data from database
        if 'form_data_page1' in request.session:
            print("form data in session\n\n")
            print("\n\n")
            #form = PageOneForm(request.session['form_data'])
            form = PageOneForm(initial=request.session.get('form_data_page1'))
        #form = PageOneForm(SESSION)
        else: #no login - create empty form
            form = PageOneForm()
            

    return render(request,
        'app/page-1.html',
        context_instance = RequestContext(request,
        {
            'title':'Graduate Application Page-1',
            'form': form,
            #'test': test,
            'year':datetime.now().year,
        }))

def page2(request):
    """Renders page2."""
    assert isinstance(request, HttpRequest)
    InstitutionsFormset = formset_factory(Institutions)
    

    #ideas
    #http://stackoverflow.com/questions/24255955/django-formsets-initializing-values-for-extra-fields-from-list-in-model-formset

    if request.method == 'POST':
        #save post data to session
        print('\n\n')
        print(request.POST) #post value example on bottom of this document
        print('\n\n')
        #print(request.POST.get('extra_field_count'))
        print('\n\n')
        form = PageTwoForm(request.POST, prefix='p2form') #, extra=request.POST.get('extra_field_count')
        formset = InstitutionsFormset(request.POST, prefix='institutions')
        request.session['form_data_page2'] = request.POST
        #request.session['extra_count'] =
        #extra=request.POST.get('extra_field_count')
        print(request.session["form_data_page2"])
        #if submit = page2 then go to page 2 else if page-3 then go to page 3
        if(request.POST.get('page1', '')):
            return HttpResponseRedirect('/page-1/')
        elif (request.POST.get('page3', '')):
            return HttpResponseRedirect('/page-3/')
        elif (request.POST.get('save', '')):
            #saveForms.savePage2(request.session['form_data_page2'])
            return HttpResponseRedirect('/page-2/') 
    # if a GET (or any other method) we'll create a blank form
    else:        
        if 'form_data_page2' in request.session:
            print("form2 data in session")
            #form = PageOneForm(request.session['form_data'])
            form = PageTwoForm(initial=request.session.get('form_data_page2'), prefix='p2form') #, request.session.get('extra_count')
            formset = InstitutionsFormset(request.session.get('form_data_page2'), prefix='institutions')
        #form = PageOneForm(SESSION)
        else: #create empty form
            formset = InstitutionsFormset(prefix='institutions')
            form = PageTwoForm(prefix='p2form')


    return render(request,
        'app/page-2.html',
        context_instance = RequestContext(request,
        {
            'title':'Graduate Application Page-2',
            'form': form,
            'formset': formset,
            'year':datetime.now().year,
        }))

def page3(request):
    """Renders page3."""
    assert isinstance(request, HttpRequest)
    
    
    if request.method == 'POST':
        #validate all forms and show errors
        #if no errors then display ready to submit and final submit button
        
        #if submit = page2 then go to page 2 else if page-3 then go to page 3
        if(request.POST.get('page1', '')):
            return HttpResponseRedirect('/page-1/')
        elif (request.POST.get('page2', '')):
            return HttpResponseRedirect('/page-2/')
        elif (request.POST.get('save', '')):
            #saveForms.savePage2(request.session['form_data_page2'])
            return HttpResponseRedirect('/page-3/') 
    # if a GET (or any other method) we'll create a blank form
    else:
        #if session exists populate form
        #form = PageOneForm(SESSION)
        #else create empty form
        #form = PageOneForm()
        print("page3")

    return render(request,
        'app/page-3.html',
        context_instance = RequestContext(request,
        {
            'title':'Graduate Application Page-3',            
            'year':datetime.now().year,
        }))

def confirmation(request):
    """Renders confirmation page."""
    assert isinstance(request, HttpRequest)
    form = PageOneForm()
    return render(request,
        'app/confirmation.html',
        context_instance = RequestContext(request,
        {
            'title':'Graduate Application Confirmation',
            'year':datetime.now().year,
            'form':form,
        }))

def pwemail(request):
   if request.method == 'GET':
       email = request.GET.get('email')  
       #seem to be issues with my localhost mailer.
       send_mail('Subject here', 'Here is the message.', 'ttkoch@noctrl.edu', [email], fail_silently=False)
       return HttpResponse("GET")
   else:
       return HttpResponse("no get")

        #return HttpResponse(
        #    json.dumps({"something to see": "this thing is happening"}),
        #    content_type="application/json"
        #)
    #else:
    #    return HttpResponse(
    #        json.dumps({"nothing to see": "this isn't happening"}),
    #        content_type="application/json"
    #    )


    
    #return render(request, 'app/pwemail.html', context_instance =
    #RequestContext(request,{}))

#def home(request):
#    """Renders the home page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/index.html',
#        context_instance = RequestContext(request,
#        {
#            'title':'Home Page',
#            'year':datetime.now().year,
#        })
#    )

#def contact(request):
#    """Renders the contact page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/contact.html',
#        context_instance = RequestContext(request,
#        {
#            'title':'Contact',
#            'message':'Your contact page.',
#            'year':datetime.now().year,
#        })
#    )

#def about(request):
#    """Renders the about page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/about.html',
#        context_instance = RequestContext(request,
#        {
#            'title':'About',
#            'message':'Your application description page.',
#            'year':datetime.now().year,
#        })
#    )


#add this to postman or json editor to make it easy to read
#{"employment_address_outside":[""],"policy_reason":[""],"employment_zip":[""],"MAX_FILE_SIZE":["2097152"],"gi":["0"],"employment_state":[""],"influenced_to_apply":[""],"planned_major":[""],"page":["Page2","Page2"],"form-TOTAL_FORMS":["3"],"form-0-ceeb":["1895"],"reference1_relationship":[""],"form-MAX_NUM_FORMS":["1000"],"form-1-undergraduate_institution":["North Central College"],"form-MIN_NUM_FORMS":["0"],"legal_reason":[""],"baseUrl":[""],"student_load_intent":[""],"form-1-ceeb":["1000"],"employer_country":["AF"],"employment_city":[""],"form-2-undergraduate_institution":["Ball State"],"tuition_remission":["0"],"page3":["Ahead to Page 3 >>"],"form-2-ceeb":["2000"],"employment_address":[""],"start_term":[""],"form-0-undergraduate_institution":["Wabash College"],"employer_address_outside_us":["0"],"reference2_name":[""],"reference1_name":[""],"resume":[""],"csrfmiddlewaretoken":["GiVvaimRmMtjC5NOczgAlxZ82Om8gfgt"],"reference2_relationship":[""],"form-INITIAL_FORMS":["0"]}

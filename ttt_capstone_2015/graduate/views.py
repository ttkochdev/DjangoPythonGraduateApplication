"""
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
from .getForms import *

from graduate.models import Race

def page1(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        #print("\n\nrequest post ", request.POST,"\n\n")
        reqpost = request.POST.copy()
        #reqpost.pop('race')
        #reqpost.setlist('race', ['2','3'])
        
        #http://stackoverflow.com/questions/21666963/django-forms-multiplechoicefield-only-selects-one-value
        #https://groups.google.com/forum/#!topic/django-users/Jg2blPdzZV4
        if 'form_data_page1' in request.session:
            del request.session['form_data_page1']            
            request.session['form_data_page1'] = reqpost
        else:            
            request.session['form_data_page1'] = reqpost

        request.session['raceinit'] = reqpost.getlist('race')
        #print('\n\nraceinit\n\n')
        #print(request.session.get('raceinit', None))
        #request.session.modified = True
        #form = PageOneForm(request.session.get('form_data_page1'), raceinit=request.session.get('raceinit'))
        #for key in request.POST:
        #    print (key)
        
        #print(form)
        #save post data to session
        #request.session['form1'] =
        
        #print("\n\nsession after post\n\n")
        #print(request.session["form_data_page1"])
        #if submit = page2 then go to page 2 else if page-3 then go to page 3
        if(request.POST.get('page2', '')):
            #form = PageOneForm(request.POST,raceinit=request.session.get('raceinit'))
            #print('\n to page 2\n')
            #if form.get('email').is_valid():  
            return HttpResponseRedirect('/page-2/')
        elif (request.POST.get('page3', '')):
            return HttpResponseRedirect('/page-3/')
        elif (request.POST.get('save', '')):
            #validate email field
            form = PageOneForm(request.session.get('form_data_page1'),raceinit=request.session.get('raceinit'))
            print('\nSAVE\n')
            if form.is_valid():  
                print("\n\nCLEANED DATA\n\n")
                cd = form.cleaned_data
                
                print(cd)
                saveForms.savePage1(request.session.get('form_data_page1'), request.session.get('raceinit'))
                return HttpResponseRedirect('/page-1/') 
            print("after is valid")
    # if a GET (or any other method) we'll create a blank form
    else:     
        
        #print(request.session.get('form_data_page1'))  
        #check if login session exists
        #if '_auth_user_id' in request.session:
        #    print("logged in")
        #    db_data = getForms.getPage1(request.session.get("_auth_user_id"))
        #    request.session['form_data_page1'] = db_data
        #    form = PageOneForm(initial=request.session.get('form_data_page1', None), raceinit=request.session.get('raceinit', None))
        #if so populate session data from database
        if 'form_data_page1' in request.session:
            print("not logged in")
            #print("\n\nform data in session\n\n")
            #print("\n\nsession before inital is set")
            #print(request.session.get('form_data_page1',None))
            #print("\n\nSESSION")
            #print("\n\nsession before inital raceinit")
            #print(request.session.get('raceinit',None))
            #print("\n\n")
            #form = PageOneForm(request.session['form_data'])
            #from django.contrib.sessions.models import Session
            #session = Session.objects.get(session_key="e625cxugewctjyae62sqbx9v30k32h1h")
            #session_data = session.get_decoded()
            #print(session_data)
           

            form_data_session = request.session.get('form_data_page1', None)
            form = PageOneForm(initial=form_data_session, raceinit=request.session.get('raceinit', None))
        #form = PageOneForm(SESSION)
        else: #no login - create empty form
            form = PageOneForm(raceinit={})
            

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
    
    #need to have email set from page 1 at least
    if not 'form_data_page1' in request.session:
        return HttpResponseRedirect('/page-1/')
    #elif 'form_data_page1' in request.session:
    #    initialsession = request.session.get('form_data_page1')
    #    print('email')
    #    print(initialsession.get('email'))
    #    if initialsession is '':

    #ideas
    #http://stackoverflow.com/questions/24255955/django-formsets-initializing-values-for-extra-fields-from-list-in-model-formset

    if request.method == 'POST':
        #save post data to session
        print('\n\n')
        #print(request.POST) #post value example on bottom of this document
        print('\n\n')
        #print(request.POST.get('extra_field_count'))
        print('\n\n')
        form = PageTwoForm(request.session.get('form_data_page2')) #, extra=request.POST.get('extra_field_count')
        formset = InstitutionsFormset(request.POST, prefix='institutions')
        request.session['form_data_page2'] = request.POST

        #request.session['extra_count'] =
        #extra=request.POST.get('extra_field_count')
        #print(request.session["form_data_page2"])
        #if submit = page2 then go to page 2 else if page-3 then go to page 3
        if(request.POST.get('page1', '')):
            return HttpResponseRedirect('/page-1/')
        elif (request.POST.get('page3', '')):
            return HttpResponseRedirect('/page-3/')
        elif (request.POST.get('save', '')):
            print("\nbefore page 2 is_valid\n")
            if formset.is_valid() and form.is_valid():
                print("\inside page 2 is_valid\n")
                instit = []            
                for i, f in enumerate(formset): 
                    cd = f.cleaned_data                    
                    undergraduate_institution = cd.get('undergraduate_institution')
                    ceeb = cd.get('ceeb')                    
                    instit.append([undergraduate_institution,ceeb])
                page1session = request.session.get('form_data_page1')                
                saveForms.savePage2(page1session.get('email'), request.session.get('form_data_page2'), instit)            
                return HttpResponseRedirect('/page-2/') 
            print("\nafter page 2 is_valid\n")
    # if a GET (or any other method) we'll create a blank form
    else:        
        if 'form_data_page2' in request.session:
            #print("form2 data in session")
            #form = PageOneForm(request.session['form_data'])

            #print("\n\n PAGE-2 SESSION \n\n")
            #print(request.session.get('form_data_page2', None))   

            form = PageTwoForm(initial=request.session.get('form_data_page2')) #, request.session.get('extra_count')
            formset = InstitutionsFormset(request.session.get('form_data_page2'), prefix='institutions')
        #form = PageOneForm(SESSION)
        else: #create empty form
            formset = InstitutionsFormset(prefix='institutions')
            form = PageTwoForm()


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
    InstitutionsFormset = formset_factory(Institutions)
    
    if request.method == 'POST':
        #validate all forms and show errors
        #if no errors then display ready to submit and final submit button
        
        page1form = PageOneForm(request.session.get('form_data_page1'),raceinit=request.session.get('raceinit'))
        page2form = PageTwoForm(request.session.get('form_data_page2'))
        page2formset = InstitutionsFormset(request.session.get('form_data_page2'), prefix='institutions')

        #if submit = page2 then go to page 2 else if page-3 then go to page 3
        if(request.POST.get('page1', '')):
            return HttpResponseRedirect('/page-1/')
        elif (request.POST.get('page2', '')):
            return HttpResponseRedirect('/page-2/')
        elif (request.POST.get('save', '')):
            #saveForms.savePage1(request.session['form_data_page1'])
            #saveForms.savePage2(request.session['form_data_page2'])
            #
            return HttpResponseRedirect('/page-3/')
        elif (request.POST.get('submit', '')):
            if page1form.is_valid() and page2form.is_valid() and page2formset.is_valid():

                return HttpResponseRedirect('/confirmation/')
    # if a GET (or any other method) we'll create a blank form
    else:
        
        if 'form_data_page1' or 'form_data_page2' in request.session:
            #print("form2 data in session")
            #form = PageOneForm(request.session['form_data'])

            #print("\n\n PAGE-2 SESSION \n\n")
            #print(request.session.get('form_data_page2', None)) 
            if 'form_data_page21' in request.session:  
                form_data_session = request.session.get('form_data_page1', None)
                page1form = PageOneForm(initial=form_data_session, raceinit=request.session.get('raceinit', None))
            if 'form_data_page2' in request.session:
                page2form = PageTwoForm(initial=request.session.get('form_data_page2')) #, request.session.get('extra_count')
                page2formset = InstitutionsFormset(request.session.get('form_data_page2'), prefix='institutions')
        else:
            page1form = PageOneForm(raceinit={})
            page2form = PageTwoForm()
            page2formset = InstitutionsFormset(prefix='institutions')
            print("new page3")

    return render(request,
        'app/page-3.html',
        context_instance = RequestContext(request,
        {
            'title':'Graduate Application Page-3',            
            'year':datetime.now().year,
            'page1form': page1form,
            'page2form': page2form,
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
        
       if Student.objects.filter(email=email).exists():
           #send_mail('Subject here', 'Here is the message.', 'ttkoch@noctrl.edu', [email], fail_silently=False)
           return HttpResponse("<p>Login with your previous session or continue to overwrite previous changes.</p><p><a href='/login'>Login to continue previous application</a></p>")
       else:
           return HttpResponse("<p>Saving a form will email you a password so that you can return to the application where you left off.</p>")       
   else:
       return HttpResponse("An Error Occurred")


import warnings

from django.conf import settings
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.template.response import TemplateResponse
from django.utils.deprecation import RemovedInDjango110Warning
from django.utils.encoding import force_text
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.utils.six.moves.urllib.parse import urlparse, urlunparse
from django.utils.translation import ugettext as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            #set session data from database
            #print("\n\nlogin\n\n")
            #print(request.session["form_data_page1"])
        #if '_auth_user_id' in request.session:
        #    print("logged in")
            page1_db_data = getForms.getPage1(request.session.get("_auth_user_id"))
            page2_db_data = getForms.getPage2(request.session.get("_auth_user_id"))
            request.session['form_data_page1'] = page1_db_data
            request.session['form_data_page2'] = page2_db_data
            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)


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

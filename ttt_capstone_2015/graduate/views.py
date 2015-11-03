"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime

from .forms import PageOneForm
from .forms import PageTwoForm

from .saveForms import *

from graduate.models import Race

def page1(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    #test = Race.objects.all() 
    #print(test)
    if request.method == 'POST':
        #print(request.POST,"\n\n")
        form = PageOneForm(request.POST)
        #for key in request.POST:
        #    print (key)
        
        #print(form)
        #save post data to session
        #request.session['form1'] = 
        request.session['form_data_page1'] = request.POST
        saveForms.savePage1(request.session['form_data_page1'])
        print(request.session["form_data_page1"])
        #if submit = page2 then go to page 2 else if page-3 then go to page 3
        if(request.POST.get('page2', '')):
            return HttpResponseRedirect('/page-2/')
        elif (request.POST.get('page3', '')):
            return HttpResponseRedirect('/page-3/')

    # if a GET (or any other method) we'll create a blank form
    else:
        #if session exists populate form
        if 'form_data_page1' in request.session:
            print("form data in session")
            #form = PageOneForm(request.session['form_data'])
            form = PageOneForm(initial=request.session.get('form_data_page1'))
        #form = PageOneForm(SESSION)
        else: #create empty form
            form = PageOneForm()

    return render(
        request,
        'app/page-1.html',
        context_instance = RequestContext(request,
        {
            'title':'Graduate Application Page-1',
            'form': form,
            #'test': test,
            'year':datetime.now().year,
        })
    )

def page2(request):
    """Renders page2."""
    assert isinstance(request, HttpRequest)


    if request.method == 'POST':
        #save post data to session
        form = PageTwoForm(request.POST)
        request.session['form_data_page2'] = request.POST
        print(request.session["form_data_page2"])
        #if submit = page2 then go to page 2 else if page-3 then go to page 3
        if(request.POST.get('page1', '')):
            return HttpResponseRedirect('/page-1/')
        elif (request.POST.get('page3', '')):
            return HttpResponseRedirect('/page-3/')

    # if a GET (or any other method) we'll create a blank form
    else:
        if 'form_data_page2' in request.session:
            print("form2 data in session")
            #form = PageOneForm(request.session['form_data'])
            form = PageTwoForm(initial=request.session.get('form_data_page2'))
        #form = PageOneForm(SESSION)
        else: #create empty form
            form = PageTwoForm()


    return render(
        request,
        'app/page-2.html',
        context_instance = RequestContext(request,
        {
            'title':'Graduate Application Page-2',
            'form': form,
            'year':datetime.now().year,
        })
    )

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

    # if a GET (or any other method) we'll create a blank form
    else:
        #if session exists populate form
        #form = PageOneForm(SESSION)
        #else create empty form
        #form = PageOneForm()
        print("page3")

    return render(
        request,
        'app/page-3.html',
        context_instance = RequestContext(request,
        {
            'title':'Graduate Application Page-3',            
            'year':datetime.now().year,
        })
    )

def confirmation(request):
    """Renders confirmation page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/confirmation.html',
        context_instance = RequestContext(request,
        {
            'title':'Graduate Application Confirmation',
            'year':datetime.now().year,
        })
    )


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
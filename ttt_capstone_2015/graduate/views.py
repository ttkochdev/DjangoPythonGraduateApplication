"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime

from .forms import PageOneForm

def page1(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        
        # create a form instance and populate it with data from the request:
        form = PageOneForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/page-2/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PageOneForm()

    return render(
        request,
        'app/page-1.html',
        context_instance = RequestContext(request,
        {
            'title':'Graduate Application Page-1',
            'form': form,
            'year':datetime.now().year,
        })
    )

def page2(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/page-2.html',
        context_instance = RequestContext(request,
        {
            'title':'Graduate Application Page-2',
            'year':datetime.now().year,
        })
    )

def page3(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
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
    """Renders the home page."""
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
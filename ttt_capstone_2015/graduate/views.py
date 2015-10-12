"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def page1(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/page-1.html',
        context_instance = RequestContext(request,
        {
            'title':'Graduate Application Page-1',
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
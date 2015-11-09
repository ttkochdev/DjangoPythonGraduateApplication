"""
Definition of urls for ttt_capstone_2015.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from graduate.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'graduate.views.page1', name='page1'),
    url(r'^page-1', 'graduate.views.page1', name='page1'), #both home and page-1 are the same
    url(r'^page-2', 'graduate.views.page2', name='page2'), 
    url(r'^page-3', 'graduate.views.page3', name='page3'), 
    url(r'^confirmation', 'graduate.views.confirmation', name='confirmation'), 
    url(r'^pwemail/$', 'graduate.views.pwemail', name='pwemail'),
    #url(r'^about', 'graduate.views.about', name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

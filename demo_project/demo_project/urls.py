from django.conf.urls import patterns, url
from django import forms
from django.views.generic import FormView

class TestForm(forms.Form):
    """An arbitrary form using most of available fields"""
    date = forms.DateField()
    date_time = forms.DateTimeField()
    time = forms.TimeField()
    number = forms.IntegerField()
    email = forms.EmailField()
    url = forms.URLField()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', FormView.as_view(template_name='home.html', 
                                form_class=TestForm)),
    # url(r'^demo_project/', include('demo_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

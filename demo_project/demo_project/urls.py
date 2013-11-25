from django.conf.urls import patterns, url
from django.http import HttpResponse
from django.template import Template, Context
from django import forms


class TestForm(forms.Form):
    """An arbitrary form using most of available fields"""
    date = forms.DateField()
    date_time = forms.DateTimeField()
    time = forms.TimeField()
    number = forms.IntegerField()
    email = forms.EmailField()
    url = forms.URLField()

def home(request):
    """View that returns the form - and nothing else"""
    tpl = Template("""{% load bootstrap_toolkit %}
                      <!DOCTYPE HTML>
                      <html>
                        <body>
                          <form class="form-horizontal" method="GET" action=".">
                            {{ form|as_bootstrap }}
                          </form>
                        </body>
                      </html>""")
    return HttpResponse(tpl.render(Context({'form': TestForm()})))

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    # url(r'^demo_project/', include('demo_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

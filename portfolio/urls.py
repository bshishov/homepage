from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.home_view, name='home_view'),
    #url(r'^project/(?P<uri>[a-zA-Z0-9\_]+)', views.project_view, name='project_view'),
    #url(r'^group/(?P<uri>[a-zA-Z0-9\_]+)', views.group_view, name='group_view'),
    #url(r'^portfolio.pdf', views.pdf_view, name='portfolio-pdf'),
    #url(r'^printable$', views.printable_view, name='printable'),

    url(r'^$', views.printable_view, name='printable'),
]

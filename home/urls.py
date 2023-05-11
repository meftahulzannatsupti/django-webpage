from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "BRACNet Admin"
admin.site.site_title = "BRACNet Admin Portal"
admin.site.index_title = "Welcome to BRACNet Admin Portal"

urlpatterns = [
    path ("",views.index, name='home'),
    path ("company",views.company, name='company'),
    path ("services",views.services, name='services'),
    path ("contact", views.contact, name='contact'),
    path ("career", views.career, name='career')

]

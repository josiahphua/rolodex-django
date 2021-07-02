from django.urls import path
from contacts.views import *

urlpatterns = [
    path('', contacts_index, name="contacts_index_page" ),
    path('show/<uuid:id>', contacts_show, name="contacts_show_page" )
] 
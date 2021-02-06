from django.urls import path
from .views import home, load_districts, load_talukas

urlpatterns = [
    path('',home,name="home"),
    path('ajax/load-districts/', load_districts, name='ajax_load_district'),
    path('ajax/load-talukas/', load_talukas, name='ajax_load_taluka'),
]

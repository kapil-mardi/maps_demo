from django.contrib import admin
from .models import State,Category,District,Taluka

# Register your models here.

admin.site.register([State,Category,District,Taluka])

from django.contrib import admin
from . models import Hobby
from . models import Portfolio
from . models import Contact

# Register your models here.

admin.site.register(Hobby)
admin.site.register(Portfolio)
admin.site.register(Contact)

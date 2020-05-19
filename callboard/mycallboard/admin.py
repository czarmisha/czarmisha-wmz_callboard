from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(AdType)
admin.site.register(Currency)
admin.site.register(City)
admin.site.register(District)
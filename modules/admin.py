from django.contrib import admin
from .models import giver_reg, taker_reg,login_table ,make_trips

# Register your models here.
admin.site.register(giver_reg)
admin.site.register(taker_reg)
admin.site.register(login_table)
admin.site.register(make_trips)

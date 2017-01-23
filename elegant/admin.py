from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.models import User, Group

from elegant.models import Client, Drug, Medication, News
from elegant.models import Procedure_name, Procedure_type, Procedure
from elegant.models import Price_category, Price

@register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ['name']

@register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_filter = ('time_start',)

# admin.site.register(Client, ClientAdmin)
admin.site.register(Medication)
admin.site.register(Drug)
admin.site.register(Procedure_type)
admin.site.register(Procedure_name)
admin.site.register(News)

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Price)


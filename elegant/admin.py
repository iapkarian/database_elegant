from django.contrib import admin
from django.contrib.auth.models import User, Group

from elegant.models import Client, Drug, Medication
from elegant.models import Procedure_name, Procedure_type, Procedure


class ClientAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ProcedureAdmin(admin.ModelAdmin):
    list_filter = ('time_start',)

admin.site.register(Client, ClientAdmin)
admin.site.register(Medication)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Drug)
admin.site.register(Procedure_type)
admin.site.register(Procedure_name)


admin.site.unregister(User)
admin.site.unregister(Group)


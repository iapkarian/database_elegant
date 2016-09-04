from django.contrib import admin
from .models import Client, Drug, Medication
from .models import Procedure_name, Procedure_type, Procedure

admin.site.register(Client)
admin.site.register(Drug)
admin.site.register(Medication)
admin.site.register(Procedure_name)
admin.site.register(Procedure)
admin.site.register(Procedure_type)




# Register your models here.

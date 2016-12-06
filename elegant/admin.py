from django.contrib import admin
from django.contrib.auth.models import User, Group

from elegant.models import Client, Drug, Medication
from elegant.models import Procedure_name, Procedure_type, Procedure


admin.site.register(Client)
admin.site.register(Medication)
admin.site.register(Procedure)
admin.site.register(Drug)
admin.site.register(Procedure_type)
admin.site.register(Procedure_name)


admin.site.unregister(User)
admin.site.unregister(Group)


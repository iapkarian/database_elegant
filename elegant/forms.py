from django import forms
from elegant.models import Procedure_name

class PostProcedure(forms.ModelForm):

    class Meta:
        model = Procedure_name
        fields = ('name', 'description', )

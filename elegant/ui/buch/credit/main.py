from django.shortcuts import render

from elegant.ui.buch.credit.forms import CreditForm
from elegant.models import Procedure_name


def start_page(request):

    return render(request, 'buch/base.html',)
                  # dict(procedure=procedure))


def in_procedure(request):

    procedure = Procedure_name.objects.all()

    return render(request, 'buch/credit.html',
                  dict(procedure=procedure))


from django.shortcuts import render

from products.models import CreditApplication
from products.utils import query_debugger


@query_debugger
def get_manufacturers_ids(request, contract_id):
    result = CreditApplication.get_manufacturers_ids_by_contract_id_vl(contract_id)

    return render(request, 'main.html', {'result': result})

from django.db import models
from django.db.models import Prefetch


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Contract(models.Model):
    contract_number = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CreditApplication(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='credit_application')
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_manufacturers_ids_by_contract_id_vl(cls, contract_id):
        result = (cls.objects.select_related('contract')
                  .get(contract_id=contract_id)
                  .products.values_list('manufacturer__id', flat=True).distinct())
        return result

    @classmethod
    def get_manufacturers_ids_by_contract_id_prr(cls, contract_id):
        credit_apps = (cls.objects.select_related('contract')
                       .prefetch_related(Prefetch('products', queryset=Product.objects.select_related('manufacturer')))
                       .get(contract_id=contract_id).products.all())
        list_man = {credit_app.manufacturer.id for credit_app in credit_apps}
        return list_man


class Product(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    credit_application = models.ForeignKey(CreditApplication, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

from django.core.management.base import BaseCommand

from products.models import Product, Contract, CreditApplication, Manufacturer


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Contract.objects.all().delete()
        CreditApplication.objects.all().delete()
        Manufacturer.objects.all().delete()

        manufacturers = [Manufacturer(name=f"manufacturer{index}") for index in range(1, 6)]
        Manufacturer.objects.bulk_create(manufacturers)

        contracts = [Contract(contract_number=index) for index in range(1, 4)]
        Contract.objects.bulk_create(contracts)
        print(f"{Contract.objects.all()}")

        creditapplications = [CreditApplication(contract=cnt) for cnt in Contract.objects.all()]
        data = CreditApplication.objects.bulk_create(creditapplications)

        manufacturers = Manufacturer.objects.all()
        creditapplications = CreditApplication.objects.all()

        products = []
        for i in range(0, 5):
            products.append(
                Product(name=f"product{i}", manufacturer=manufacturers[i], credit_application=creditapplications[0]))
        Product.objects.bulk_create(products)

        products = []
        for i in range(5, 10):
            products.append(
                Product(name=f"product{i}", manufacturer=manufacturers[0], credit_application=creditapplications[1]))
        Product.objects.bulk_create(products)

        products = []
        for i in range(10, 15):
            products.append(
                Product(name=f"product{i}", manufacturer=manufacturers[3], credit_application=creditapplications[2]))
        Product.objects.bulk_create(products)

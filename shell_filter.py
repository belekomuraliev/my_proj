from my_app.models import Customer, Work, Account

customer_icloud = Customer.objects.filter(email__icontains='icloud.com')
print(customer_icloud)

company_ltd = Work.objects.filter(company__icontains='Ltd')
print(company_ltd)

protonmail = Account.objects.filter(customer__email__icontains='protonmail')
print(protonmail)





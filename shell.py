from my_app.models import Customer, Work, Account

import json


with open("data_hw.json", "r") as file:
    data = json.load(file)

for create in data:

    create_customer=Customer.objects.create(
        name=create['name'], phone=create['phone'], email=create['email']
    )
    create_work=Work.objects.create(
        address=create['address'], city=create['city'], company=create['company'],
        postalZip=create['postalZip'],
    )
    create_account=Account.objects.create(
        pin=create['pin'], acc_num=create['acc_num'], pan=create['pan'],
        cvv=create['cvv']
    )






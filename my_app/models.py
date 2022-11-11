from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Work(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    postalZip = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1, blank=True)

    def __str__(self):
        #return f'{self.customer.name} - Address: ({self.address}) - City: {self.city}'
        return f'{self.customer.name}, - Company: {self.company}'
class Account(models.Model):
    pin = models.IntegerField()
    acc_num = models.CharField(max_length=20)
    pan = models.CharField(max_length=30)
    cvv = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1, blank=True)

    def __str__(self):
        return f'{self.customer.name} - acc_num {self.acc_num}'





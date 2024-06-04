from django.db import models

# Create your models here.

# User Model
class User(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=20)
    phone_Number = models.CharField(max_length=11)
    email = models.EmailField(max_length=120)

    def __str__(self):
        return f'{self.username} {self.password} {self.phone_Number} {self.email}'

class Budget(models.Model):
    budget_name = models.CharField(max_length=120)
    budget_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    budget_date = models.DateTimeField(auto_now_add=True)
    # expires_at = models.DateTimeField(null=True, blank=True) 
    status = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.budget_name}'

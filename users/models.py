from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# AbstractUser o AbstractBaseUser(id, password, last_login)

class User(AbstractUser):
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property    
    def shipping_address(self):
        return self.shippingaddress_set.filter(default=True).first()

    def has_shipping_address(self):
        return self.shipping_address is not None

class Customer(User):
    class Meta:
        proxy = True # El modelo no generara una nueva tabla en la base de datos
    
    def get_products(self):
        return []

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

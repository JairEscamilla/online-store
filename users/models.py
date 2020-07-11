from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(User):
    class Meta:
        proxy = True # El modelo no generara una nueva tabla en la base de datos
    
    def get_products(self):
        return []

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    
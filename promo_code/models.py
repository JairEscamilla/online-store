from django.db import models
from django.db.models.signals import pre_save
import string 
import random

# Create your models here.
class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.FloatField(default=0.0)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
    
    def use(self):
        self.used = True
        self.save()
    
def set_code(sender, instance, *args, **kwargs):
    if instance.code:
        return 
    
    chars = string.ascii_uppercase + string.digits
    instance.code = ''.join(random.choice(chars) for _ in range(10))


pre_save.connect(set_code, sender=PromoCode)
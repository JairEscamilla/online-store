from django.db import models
from users.models import User

class BillingProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=50, null=False, blank=False)
    cart_id = models.CharField(max_length=50, null=False, blank=False)
    last4 = models.CharField(max_length=4, null=False, blank=False)
    brand = models.CharField(max_length=10, null=False, blank=False)

    default = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
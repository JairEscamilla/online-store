from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50, )
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #def save(self, *args, **kwargs):
    #    self.slug = slugify(self.title)
    #    super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

def set_slug(sender, instance, *args, **kwargs): #callback
    instance.slug = slugify(instance.title)


pre_save.connect(set_slug, sender=Product)
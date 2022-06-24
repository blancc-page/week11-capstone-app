from django.forms import SlugField
from django.shortcuts import reverse
from pyexpat import model
from django.db import models
from django.conf import settings
# Create your models here.

CATEGORY_CHOICES = (
    ('S','Shirt'),
    ('SW', 'SportWear'),
    ('OW', 'OuterWear'),
)

LABEL_CHOICES = (
    ('P','primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discounted_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, blank=True) 
    label = models.CharField(choices=LABEL_CHOICES, max_length=1,blank=True)
    slug = models.SlugField()
    description = models.TextField()
    

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('ecommerceApp:product', kwargs={
            'slug': self.slug
        })
    
    def get_add_to_cart_url(self):
        return reverse('ecommerceApp:add_to_cart', kwargs={
            'slug': self.slug
        })
    def get_remove_from_cart_url(self):
        return reverse('ecommerceApp:remove_from_cart', kwargs={
            'slug': self.slug
        })
        

class OrderItem(models.Model):
    user = models.user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date= models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

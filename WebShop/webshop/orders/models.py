from django.db import models
from items.models import Item
from django.contrib.auth.models import User
from django.utils import timezone


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    create = models.DateTimeField(null=False, default=timezone.now)
    complete = models.DateTimeField(null=True)
    status = models.CharField(max_length=100)


class Purchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.item.product.name}'

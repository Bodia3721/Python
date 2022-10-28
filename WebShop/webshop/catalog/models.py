from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return str(self.name)


class Producer(models.Model):

    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return str(self.name)


class Product(models.Model):

    name = models.CharField(max_length=100, null=False)
    about = models.TextField(max_length=500, null=False)
    picture = models.FileField(upload_to='pictures/', null=False)
    price = models.FloatField(null=False)
    count = models.IntegerField(null=False)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

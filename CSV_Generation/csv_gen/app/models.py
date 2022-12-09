from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

CHOICES = (

    ('1', 'Choose...'),
    ('2', 'name'),
    ('3', 'job'),
    ('4', 'company'),
    ('5', 'date'),
    ('6', 'phone'),
    ('7', 'address'),
    ('8', 'city'),
    ('9', 'country'),
    ('10', 'email')

    )


class Scheme(models.Model):

    upload = models.FileField(upload_to='', blank=True)

    name = models.CharField(max_length=30, default="None", blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    col1 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")
    col2 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")
    col3 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")
    col4 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")
    col5 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")
    col6 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")
    col7 = models.CharField(max_length=30, choices=CHOICES, default="Choose...")

    name1 = models.CharField(max_length=30, default="None", blank=True)
    name2 = models.CharField(max_length=30, default="None", blank=True)
    name3 = models.CharField(max_length=30, default="None", blank=True)
    name4 = models.CharField(max_length=30, default="None", blank=True)
    name5 = models.CharField(max_length=30, default="None", blank=True)
    name6 = models.CharField(max_length=30, default="None", blank=True)
    name7 = models.CharField(max_length=30, default="None", blank=True)

    ord1 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    ord2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    ord3 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    ord4 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    ord5 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    ord6 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])
    ord7 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(9)])

    rows = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name + ' (' + str(self.author) + ')' + ' (id ' + str(self.id) + ')'


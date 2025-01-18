from django.db import models

# Create your models here.
from mongoengine import Document, fields

class User(Document):
    username = fields.StringField(required=True)
    password = fields.StringField(required=True)

class AdminUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
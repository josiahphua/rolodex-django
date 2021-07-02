from django.db import models
import uuid

# Create your models here.
class Contact(models.Model):
    id = models.UUIDField(
        primary_key = True,
        editable = False,
        default = uuid.uuid4
    )
    name = models.CharField(max_length=100, null=False)
    number = models.CharField(max_length=50, null=False)
    description = models.TextField()
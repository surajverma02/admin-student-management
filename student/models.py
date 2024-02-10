from django.db import models
import uuid

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField(null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
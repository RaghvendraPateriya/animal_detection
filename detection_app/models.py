import uuid
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    secret_key = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


class AnimalImage(models.Model):
    label = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.BigIntegerField()
    subject = models.CharField(max_length=1000)
    message = models.TextField()
    policy = models.BooleanField(default=False)

    def __str__(self):
        return self.name
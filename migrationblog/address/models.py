from unittest.util import _MAX_LENGTH
from django.db import models


class AddressBook(models.Model):
    name = models.CharField(max_length=200)
    telephone_number = models.CharField(max_length=25)
    postcode = models.CharField(max_length=25, default="00000")

    def __str__(self):
        return self.name

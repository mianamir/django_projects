from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name} {self.description}'

    def __repr__(self):
        return f'ID={self.id} Name={self.name}'

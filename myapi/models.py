from django.db import models


class Drink(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    rate = models.TextField(blank=True,null=True)


    def __str__(self):
        return self.name +' '+self.description+' '+self.rate


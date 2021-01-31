from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name +', '+ str(self.age)

    
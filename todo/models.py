from django.db import models

class db(models.Model):
    name = models.CharField(max_length=40)
    gg = models.BooleanField(default=True)


    def __str__(self) :
        return self.name  
    


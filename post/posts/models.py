from django.db import models

# Create your models here.
class Post(models.Model): #Creamos la clase Post con un modelo de texto
    message = models.TextField()
    
    def __str__(self): #Junto con una función que nos permitirá ver el mensaje que escribimos
        return self.message[:50]
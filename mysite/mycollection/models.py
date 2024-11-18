from django.db import models

class Telephone(models.Model):
    marque = models.CharField(max_length=200)
    modele = models.CharField(max_length=200)
    prix = models.IntegerField()
    coloris = models.CharField(max_length=50)
    
    def __str__(self):
        return self.marque + ' ' + self.modele +' ' + self.coloris + ' ' + str(self.prix)
    
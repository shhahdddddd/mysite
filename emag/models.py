from django.db import models
from datetime import date

class Categorie(models.Model):
    TYPE_CHOICES = [
        ('Al', 'Alimentaire'), ('Mb', 'Meuble'),
        ('Sn', 'Sanitaire'), ('Vs', 'Vaisselle'),
        ('Vt', 'Vêtement'), ('Jx', 'Jouets'),
        ('Lg', 'Linge de Maison'), ('Bj', 'Bijoux'),
        ('Dc', 'Décor')
    ]
    name = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Al')

    def __str__(self):
        return self.name

class Produit(models.Model):
    TYPE_CHOICES = [
        ('em', 'Électroménager'),
        ('cs', 'Consommable'),
        ('fr', 'Frais'),
        ('mb', 'Meuble'),
    ]
    libelle = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='cs')

    def __str__(self):
        return self.libelle


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

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, blank=True)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=8)

    def __str__(self):
        return self.nom

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
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='cs')
    img = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.libelle

class ProduitNC(Produit):
    duree_garantie = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.libelle} - Garantie: {self.duree_garantie}"

class Commande(models.Model):
    dateCde = models.DateField(null=True, default=date.today)
    totalCde = models.DecimalField(max_digits=10, decimal_places=3)
    produits = models.ManyToManyField(Produit)

    def __str__(self):
        return f"Commande du {self.dateCde} - Total: {self.totalCde}"
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Produit,Commande
from .forms import ProduitForm, CommandeForm,FournisseurForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from datetime import date
from decimal import Decimal
from .forms import UserRegistrationForm
def vitrine(request):
    list_produits = Produit.objects.all()
    return render(request, 'magasin/vitrine.html', {'list': list_produits})

def maj_produits(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)  # Handle file uploads (images)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/')
    else:
        form = ProduitForm()
    return render(request, 'magasin/majProduits.html', {'form': form})

def acceuil(request):
    return render(request, 'magasin/acceuil.html')
@login_required
def ajouter_commande(request):
    if request.method == "POST":
        form = CommandeForm(request.POST)
        if form.is_valid():
            # Get form data
            produit = form.cleaned_data['produit']
            quantite = form.cleaned_data['quantite']
            # Calculate total (example: totalCde = produit.prix * quantite)
            total_cde = produit.prix * quantite
            # Create Commande
            commande = Commande.objects.create(
                dateCde=date.today(),
                totalCde=total_cde
            )
            # Add produit to the ManyToManyField
            commande.produits.add(produit)
            return HttpResponseRedirect('/magasin/')
    else:
        form = CommandeForm()
    return render(request, 'magasin/ajouterCommande.html', {'form': form})
@login_required
def ajouter_fournisseur(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST)
        if form.is_valid():
            fournisseur = form.save(commit=False)
            fournisseur.save()
            # Update the fournisseur field for selected produits
            produits = form.cleaned_data['produits']
            produits.update(fournisseur=fournisseur)
            return HttpResponseRedirect('/magasin/')
    else:
        form = FournisseurForm()
    return render(request, 'magasin/ajouterFournisseur.html', {'form': form})
@login_required
def home(request):
   return render(request, 'magasin/acceuil.html')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
from django import forms
from django.forms import ModelForm
from .models import Produit,Commande,Fournisseur
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"

class CommandeForm(forms.Form):
    produit = forms.ModelChoiceField(queryset=Produit.objects.all(), label="Produit")
    quantite = forms.IntegerField(min_value=1, label="Quantité")
class FournisseurForm(forms.ModelForm):
    produits = forms.ModelMultipleChoiceField(
        queryset=Produit.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Produits associés"
    )
    class Meta:
        model = Fournisseur
        fields = ['nom', 'prenom', 'email', 'telephone', 'adresse', 'produits']
        widgets = {
            'adresse': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        if not telephone.isdigit() or len(telephone) != 8:
            raise forms.ValidationError("Le téléphone doit être un numéro de 8 chiffres.")
        return telephone
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

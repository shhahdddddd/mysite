from rest_framework import viewsets
from emag.models import Categorie, Produit
from emag.serializers import CategorySerializer, ProduitSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Produit with full CRUD support.
    """
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

    def get_queryset(self):
        queryset = Produit.objects.all()
        category_id = self.request.query_params.get('categorie_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Categorie with full CRUD support.
    """
    queryset = Categorie.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Categorie.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

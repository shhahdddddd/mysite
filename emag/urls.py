# emag/urls.py
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductViewSet, CategoryViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = SimpleRouter()
router.register(r'produit', ProductViewSet, basename='produit')
router.register(r'categorie', CategoryViewSet, basename='categorie')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),  # important!
]

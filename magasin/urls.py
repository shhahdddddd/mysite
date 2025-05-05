from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.vitrine, name='vitrine'),  # Updated to use vitrine
    path('maj/', views.maj_produits, name='maj_produits'),
    path('ajouter-commande/', views.ajouter_commande, name='ajouter_commande'), 
    path('ajouter-fournisseur/', views.ajouter_fournisseur, name='ajouter_fournisseur'),
    path('register/', views.register, name='register'),# Fixed view name here
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

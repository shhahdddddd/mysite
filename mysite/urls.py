from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from magasin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('magasin/', include('magasin.urls')),
    path('blog/', include('blog.urls')),
    path('', views.home, name='home'), 
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  
    path('api/', include('emag.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
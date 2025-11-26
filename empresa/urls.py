from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from empresa import views  # Importa do arquivo views.py corretamente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rh.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('cupom/', views.cupom, name='cupom'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

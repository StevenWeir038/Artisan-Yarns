from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('contact/', include('contact.urls')),
    path('profile/', include('profiles.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('basket/', include('basket.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'artisan_yarns.views.handler404'
handler500 = 'artisan_yarns.views.handler500'

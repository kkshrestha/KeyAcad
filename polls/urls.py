from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views 
urlpatterns = [
    path('home/', views.home, name="home"),
    path('index/', views.index, name="home"),
    path('view-certificate/', views.viewcertificate, name="home"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
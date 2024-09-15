from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views 
from django.contrib import admin
from .views import home

urlpatterns = [
    path('', views.home, name="home"),
    path('view-certificate/', views.viewcertificate, name="home"),
    path('about_us/',views.about_us, name="about_us"),
    path('Course/<slug:slug>/', views.course_detail, name="course_detail"),
    path('register/', views.register, name="register"),
    path('login/', home, name='login'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
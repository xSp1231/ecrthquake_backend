from django.urls import path,include
from datamanage import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('getprovincedata/',views.getprovincedata),
    path('getprovinceintro/',views.getprovinceintro),
    path('getmagnitudedata/',views.getmagnitudedata),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
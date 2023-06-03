from django.urls import path,include
from datamanage import views
urlpatterns = [
    path('getprovincedata/',views.getprovincedata)
]
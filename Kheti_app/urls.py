from django.urls import path
from . import views

urlpatterns = [
path('',views.Home, name = 'Home'),
path('Crop_recommend',views.Crop_recommend , name = 'Crop_recommend'),
path('crop_prediction',views.crop_prediction , name = 'crop_prediction'),
path('Fertilizer_recommendation', views.Fertilizer_recommendation, name = 'Fertilizer_recommendation'),
path('Disease_prediction', views.Disease_prediction, name = 'Disease_prediction'),
path('Home',views.Home, name = 'Home'),
path('Fertilizer_prediction', views.Fertilizer_prediction, name = 'Fertilizer_prediction'),
path('sign',views.sign , name = 'sign' ),

]
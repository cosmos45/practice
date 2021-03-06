from . import views
from django.urls import path

app_name = 'dynamicnav'

urlpatterns = [
    path('', views.dyna, name='dyna'),
    path('dyna/', views.dyna, name='dyna'),
    path('wildlifepaintings/', views.wildlifepaintings, name='wildlifepaintings'),
    path('pastelpaintings/', views.pastelpaintings, name='pastelpaintings'),
    path('inkpaintings/', views.inkpaintings, name='inkpaintings'),
    path('abstract_description/<int:id>', views.abstract_description, name='abstract_description'),
    path('wildlife_description/<int:id>', views.wildlife_description, name='wildlife_description'),

]

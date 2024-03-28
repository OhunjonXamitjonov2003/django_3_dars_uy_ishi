from django.urls import path
from .views import all_cars,cars_by_brends,cars_by_colors




urlpatterns = [
 path('',all_cars,name='index'),
 path('brand/<int:brand_id>/',cars_by_brends,name='marka'),
 path('color/<int:color_id>/',cars_by_colors,name='rang'),

]
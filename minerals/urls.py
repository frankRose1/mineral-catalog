from django.urls import path
from . import views

app_name = 'minerals'

urlpatterns = [
    path('', views.mineral_list, name='list'),
    path('minerals/', views.mineral_list, name='filtered_list'),
    path('mineral/<int:mineral_id>/', views.mineral_detail, name="detail"),
    path('search/', views.search, name='search')
]

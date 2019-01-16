from django.urls import path
from . import views

app_name = 'minerals'

urlpatterns = [
    path('', views.mineral_list, name='list'),
    path('<int:mineral_id>/', views.mineral_detail, name="detail")
]

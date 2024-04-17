from django.urls import path
from articles import views

urlpatterns = [
    path('', views.articles),
    path('create/', views.create),
    path('read/', views.read),
    path('read/<int:id>/', views.read_id),
    path('create-person/', views.create_person),
    path('read-person/', views.read_person),
    path('read-person/<int:id>/', views.read_id_person),

]

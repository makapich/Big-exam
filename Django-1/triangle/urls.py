from django.urls import path

from . import views

app_name = 'triangle'
urlpatterns = [
    path('triangle/', views.triangle, name='triangle'),
    path('person/', views.person_list, name='person'),
    path('person/register', views.person_register, name='person_register'),
    path('person/<int:pk>/', views.person_update, name='person_update'),
]

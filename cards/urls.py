from django.urls import path
from . import views

urlpatterns = [
    path('collection/', views.CollectionList.as_view()),
]
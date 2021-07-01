from django.urls import path
from . import views

urlpatterns = [
    path('collection/', views.CollectionList.as_view()),  # GET all/POST Collections
    path('collection/card/', views.CardList.as_view()),  # GET all Cards
    path('collection/card/<int:collection>/new/', views.CardList.as_view()),  # Card POST by Collection ID
    path('collection/card/<int:collection>/', views.CardDetail.as_view()),  # Card GET by Collection ID
    path('collection/card/<int:pk>/update/', views.CardEdit.as_view()),  # Card PUT
    path('collection/card/<int:pk>/delete/', views.CardEdit.as_view()),  # Card DELETE
]
#words_game
#groups/urls.py

from django.urls import path
from . import views

app_name = 'game_app'


urlpatterns = [
    path('descriptions/', views.DescriptionList.as_view(), name = 'game'),
    path('descriptions/<int:pk>/', views.GuessingPage.as_view(), name = 'guessing_page'),
]

from django.urls import path
from recipe.views import *

app_name = 'recipe'
urlpatterns = [
    path('create/', RecipeCreateView.as_view()),
    path('list/', RecipeListView.as_view()),
    path('<int:pk>/', RecipeRetrieveUpdateDestroyView.as_view()),
]

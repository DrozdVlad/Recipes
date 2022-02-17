from django.db.models import F
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from recipe.filters import RecipeFilter
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer


class RecipeCreateView(generics.CreateAPIView):
    serializer_class = RecipeSerializer


class RecipeListView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']
    filterset_class = RecipeFilter


class RecipeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def get(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(id=kwargs['pk'])
        recipe.count_of_views = F('views') + 1
        recipe.save()
        return self.retrieve(request, *args, **kwargs)

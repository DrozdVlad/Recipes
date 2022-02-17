from django_filters import rest_framework as filters

from recipe.models import Recipe


class RecipeFilter(filters.FilterSet):
    views_gte = filters.NumberFilter(field_name="views", lookup_expr='gte')
    views_lte = filters.NumberFilter(field_name="views", lookup_expr='lte')

    class Meta:
        model = Recipe
        fields = ['creator', 'views']
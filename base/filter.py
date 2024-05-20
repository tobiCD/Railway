from django_filters import CharFilter
from .models import *
import django_filters
from django import forms

class Postfilter(django_filters.FilterSet):
    headline = CharFilter(field_name='headline', lookup_expr="icontains", label='Headline')
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),
    widget=forms.CheckboxSelectMultiple )
    class Meta :
        model = Post
        fields = ["headline","tags"]
from django.urls import path
from .views import ItemListCreateView

urlpatterns = [
    path('item/', ItemListCreateView.as_view(), name='item-list-create'),
]
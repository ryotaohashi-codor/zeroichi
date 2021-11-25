from django.urls import path

from . import views

urlpatterns = [
    path("", views.ItemListView.as_view(), name='item-list'),
    path('create/', views.ItemCreateView.as_view(), name='item-create'),
    path('check/<int:pk>/', views.ItemCheckView.as_view(), name='item-check'),
]
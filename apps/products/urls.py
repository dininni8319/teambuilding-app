from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_all, name='product-list'),
    path('add/', views.create, name='product-create'),
    path('<int:pk>/edit/', views.update, name='product-update'),
    path('<int:pk>/delete/', views.delete, name='product-delete'),
    path('producers/', views.producer_list_all, name='product-producer-list'),
    path('producers/add/', views.producer_create, name='product-producer-create'),
    path('producers/add/<str:country>/', views.producer_create, name='product-producer-create'),
    path('producers/<int:pk>/delete/', views.producer_delete, name='product-producer-delete'),
    path('producers/<int:pk>/edit/', views.producer_update, name='product-producer-update'),
    path('producers/<int:pk>/edit/<str:country>/', views.producer_update, name='product-producer-update'),
    path('<int:product_id>/edit/options/add/', views.purchase_option_create, name='product-purchase-option-create'),
    path('_/edit/options/<int:pk>/delete/', views.purchase_option_delete,name='product-purchase-option-delete'),
    path('<int:product_id>/edit/options/<int:pk>/delete/', views.purchase_option_delete, name='product-purchase-option-delete'),
    path('_/edit/options/<int:pk>/edit/', views.purchase_option_update, name='product-purchase-option-update'),
    path('<int:product_id>/edit/options/<int:pk>/edit/', views.purchase_option_update, name='product-purchase-option-update'),
]

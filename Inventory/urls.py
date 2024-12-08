from django.urls import path
from .views import *

urlpatterns = [
    path('products/', product_list.as_view(), name="products"),
    # path('products/add/', product_add.as_view()),
    # path('products/<int:id>/', product_detail.as_view()),
    # path('products/<int:id>/update/', product_update.as_view()),
    # path('products/<int:id>/delete/', product_delete.as_view()),
    path('categories/', category_list.as_view() , name='categories'),
    # path('categories/add/', category_add.as_view()),
    path('categories/<int:id>/', category_items.as_view() , name= 'category'),
    # path('categories/<int:id>/update/', category_update.as_view()),
    # path('categories/<int:id>/delete/', category_delete.as_view()),
    path('cart/', cart_list.as_view() , name='cart'),
    path('cart/add/<int:id>/', cart_add.as_view() , name='cart_add'),
    # path('cart/<int:id>/update/', cart_update.as_view()),
    # path('cart/<int:id>/delete/', cart_delete.as_view()),
]


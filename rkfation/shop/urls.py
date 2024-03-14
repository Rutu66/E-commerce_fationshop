from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('address/', views.address, name='address'),
    path('order/', views.order, name='order'),

    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('registration/', views.registraion, name='registration'),
    path('logout/', views.user_logout, name='logout'),

    
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('product/<int:id>/', views.product_details, name='product_details'),
    path('category/<int:id>/', views.category_details, name='category_details'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_quantity/<int:cart_id>',views.add_quantity, name = 'add_quantity'),
    path('remove_quantity/<int:cart_id>',views.remove_quantity, name = 'remove_quantity'),
    path('delete_item/<int:cart_id>',views.delete_iteam, name = 'delete_item'),
    path('add_to_cart/<int:id>/',views.add_to_cart, name = 'add_to_cart'),
    path('add_address/',views.add_address, name = 'add_address')
    

    
]

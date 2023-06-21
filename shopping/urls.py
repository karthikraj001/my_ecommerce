from django.urls import path
from . import views

from shopping import cart, checkout

urlpatterns = [
    path('', views.index, name='index'),
    path('collections/', views.collections, name="collections"),
    path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),
    path('login/', views.login, name='loginpage'),
    path('registration/', views.registration, name='registration'),
    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('cart', cart.viewcart, name="cart"),
    path('main/', views.main, name='main'),
    path('update-cart/', cart.updatecart, name='updatecart'),
    path('delete-cart-item/', cart.deletecartitem, name='deletecartitem'),
    path('checkout/', checkout.index, name='checkout'),
    path('place-order/', checkout.placeorder, name='placeorder'),
    path('proceed-to-pay/', checkout.razorpaycheck),
    path('my-orders/', checkout.orders),

    path('product-list', views.productlistAjax),
    path('searchproduct', views.searchproduct, name="searchproduct")
]

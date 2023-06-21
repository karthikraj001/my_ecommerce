from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from shopping import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('about/', views.about,name='about'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('payment/', views.payment, name='payment'),
    path('logout/', views.logout, name='logout'),

    path('', include('shopping.urls')),
    path('collections/', views.collections, name='collections'),
    path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),

    path('logout/', views.logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
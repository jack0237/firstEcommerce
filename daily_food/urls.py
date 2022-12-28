from django import views
from django.urls import path, include
from accounts.views import signup, logout_user, login_user, add_to_cart 
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('<int:myid>', detail, name="detail"), # url dynamique qui change selon les id pour aficher les details des produits
    path('<str:slug>', add_to_cart, name="add-to-cart"),
    #path('<str:slug>/', product_detail, name="product-detail"),
    path('signup/', signup, name="signup"),
    path('logout/', logout_user, name="logout"),
    path('login/',login_user, name="login"),

]
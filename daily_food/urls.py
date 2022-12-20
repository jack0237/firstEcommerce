from django import views
from django.urls import path,include
from accounts.views import signup
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('<int:myid>', detail, name="detail"), # url dynamique qui change selon les id pour aficher les details des produits
    path('signup/', signup, name="signup"),
    path('login',login, name="login"),

]
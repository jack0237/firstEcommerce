from django import views
from django.urls import path,include
from accounts.views import signup, logout_user, login_user
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('<int:myid>', detail, name="detail"), # url dynamique qui change selon les id pour aficher les details des produits
    path('signup/', signup, name="signup"),
    path('logout/', logout_user, name="logout"),
    path('login/',login_user, name="login"),

]
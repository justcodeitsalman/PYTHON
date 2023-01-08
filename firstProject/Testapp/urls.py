from django.contrib import admin
from django.urls import path
from Testapp import views


urlpatterns = [
    #path('',views.Hello_World_Fun),
    path('',views.main),
    path('join/', views.join),
    path('login/', views.Login)

]

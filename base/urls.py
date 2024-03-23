from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("room/<str:pk>/",views.room,name="room"),
    path("create-room/",views.create_room,name="create-room"),
    path("my-rooms/",views.my_room,name="my-room"),
    path('update-room/<str:pk>/',views.update_room,name="update-room"),
    path('deleteroom/<str:pk>/',views.delete,name="delete-room"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutPage,name="logout"),
    
]
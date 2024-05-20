from django.conf import settings
from django.urls import path ,include
from . import views
from django.conf.urls.static import static


urlpatterns =[
    path('',views.home,name='home'),
    path('', views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('post/<slug:slug>/', views.POST, name="post"),
    path('profile/', views.profile, name="profile"),

    #CRUD
    path('create_post/', views.create_Post, name='create_post'),
    path('update_post/<slug:slug>/', views.update_Post, name='update_post'),
    path('delete_post/<slug:slug>/', views.delete_Post, name='delete_post'),
    path('send_email/', views.send_email, name='send_email'),
    
    #Authentication
    path('login/', views.LoginView, name='login'),
    path('register/',views.Register  , name = 'register'),
    path('logout/',views.Logout  , name = 'logout'),
    path('todolist/',views.Todolist , name='todolist')



]+ static(settings.STATIC_URL, document_root=settings.STATIC_URL)
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('delete_user/<int:pk>', views.DeleteUser.as_view(), name='delete_user'),
    path('logout/', views.LogoutPage, name='logout'),

]

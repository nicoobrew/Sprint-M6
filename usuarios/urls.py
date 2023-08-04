from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios import views as vistas_usuarios

app_name = 'usuarios'

urlpatterns = [
    path("registro/", vistas_usuarios.registro, name="registro"),
    path("login/", auth_views.LoginView.as_view(template_name = 'usuarios/login.html'), name="login"), 
    path("logout/", auth_views.LogoutView.as_view(template_name = 'usuarios/logout.html'), name="logout"),    
]

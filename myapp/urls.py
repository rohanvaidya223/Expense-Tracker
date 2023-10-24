from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.index,name='index'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',auth_view.LogoutView.as_view(template_name='myapp/logout.html'),name='logout')
]

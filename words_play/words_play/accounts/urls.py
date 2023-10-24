#words_play

from django.urls import path
from django.contrib.auth import views as auth_views # is automatically providing build in login/logout views.
from accounts import views

app_name = 'accounts'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),# it goes to homepahe
    path('signup/', views.SignUp.as_view(), name = 'signup'),

]

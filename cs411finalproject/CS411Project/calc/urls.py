from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('updatePage', views.updatePage, name='updatePage'),
    path('create', views.createProfilePage, name='create'),
    path('profile', views.viewProfile, name='profile'),
    path('gettingInputFromCreate', views.gettingInputFromCreate, name='gettingInputFromCreate'),
    path('deletePerson', views.deletePerson, name='deletePerson'),
    path('preferencePerson', views.preferencePerson, name='preferencePerson'),
    path('updateProfile', views.updateProfile, name='updateProfile'),
    path('suggestions', views.suggestions, name='suggestions'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('allusers', views.allusers, name='allusers'),
    path('login_action', views.login_action, name='login_action')

]

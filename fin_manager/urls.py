#from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('expenses', name='expenses', view=views.ExpenseListView.as_view()),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]

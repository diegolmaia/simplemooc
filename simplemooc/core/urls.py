from django.urls import path
from . import views

urlpatterns = [
	#path('<>', arquivo.funcao, nome)
    path('', views.home, name='home'),
    path('contato/', views.contact, name='contact'),
]
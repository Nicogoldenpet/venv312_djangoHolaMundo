from django.urls import path
from .views import HomePageView

#Damos una URL
urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]
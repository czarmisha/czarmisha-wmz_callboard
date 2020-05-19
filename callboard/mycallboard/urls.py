from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('', AdsList.as_view(), name='home'),
    path('category/<int:pk>/', AdsCategoryList.as_view(), name='category'),
    path('create_ad/', CreateAd.as_view(), name='create_ad'),
    path('create_ad/success', create_success, name='create_success'),
]
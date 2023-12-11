from django.urls import path
from . import views
from .views import MyTokenObtainedPairView

urlpatterns = [
    path('', views.getUser),
    path('token/', MyTokenObtainedPairView.as_view(), name='token_obtain_pair'),
    path('users/', views.getUsers),
    path('users/signup/', views.signUpUser)
]
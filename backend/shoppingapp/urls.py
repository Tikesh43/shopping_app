from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   # login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh token
   
    path('user_delete/<int:pk>', UsersUpdateView.as_view(), name="user delete"),
    path('users/', UsersView.as_view(), name='users_api'),
    path('role-based/', RoleBasedView.as_view(), name='role_based_view'),
    
    path("product/", ProductAdd.as_view(), name="ADD Product"),
    path("product/<int:pk>", ProductAdd.as_view(), name="ADD Product"),

    path("category/", CategoryAdd.as_view(), name="Create Category"),
]

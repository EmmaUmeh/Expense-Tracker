from django.contrib import admin
from django.urls import path
from expenses.views import *
from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
     # Endpoint to obtain JWT token
     path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/login', Login_User, name='login'),  # Login endpoint (using JWT)
    path('auth/register', Register_User, name='register'),  # Registration endpoint
     path('create/budget', CreateBudget, name='budget'),  # Registration endpoint
]

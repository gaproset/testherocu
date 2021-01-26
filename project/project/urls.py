"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include 
from ekdilwsi import views     
from rest_framework import routers  
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()                      # add this
router.register(r'ekdilwsiview', views.Ekdilwsi2View, 'ekdilwsi') 
router.register(r'inviteview', views.InviteView, 'invite') 
router.register(r'users', views.UserView,'user')
router.register(r'attendanceloggerview', views.attendanceloggerView, 'logger') 
router.register(r'libraryView', views.libraryView, 'library') 
router.register(r'partnersView', views.partnersView, 'partners') 
router.register(r'partnersTypeView', views.partnersTypeView, 'parterstype') 


urlpatterns = [
    path('admin/', admin.site.urls),    
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/', include('ekdilwsi.urls')),
    path('api/', include(router.urls)),
    # path('api/auth/', include('users.urls')),
    path('api/token-auth/', obtain_jwt_token),
    path('auth/', include('rest_framework.urls')),
      path('api/auth/', include('ekdilwsi.urls')),
    # path('api/logoupload', views.LogoUpload.as_view()),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # new
    # path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/jwtauth/', include('jwtauth.urls'), name='jwtauth'), # new   

]


# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

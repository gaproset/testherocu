from django.urls import path
import ekdilwsi.views as views
from .views import Ekdilwsi2View, EkdilwsiView, InviteView,current_user, UserList


urlpatterns = [
    # path('ekdilwsi/', views.EkdilwsiView.as_view()),
    #  path('invite/', views.InviteView.as_view()),
    # path('ekdilwsiView/', Ekdilwsi2View)
     path('current_user/', current_user),
    path('users/', UserList.as_view())
]
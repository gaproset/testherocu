from django.shortcuts import render
from rest_framework import viewsets   
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ekdilwsi
from .models import Invite
from .models import partnersType
from .models import partners
from .models import library
from .models import attendancelogger


from .serializers import EkdilwsiSerializer  
from .serializers import InviteSerializer  
from .serializers import partnersTypeSerializer  
from .serializers import partnersSerializer 
from .serializers import attendanceloggerSerializer  
from .serializers import librarySerializer 

from .serializers import GroupSerializer 
from .serializers import UserSerializer 
from .serializers import PermissionSerializer

from .serializers import  UserSerializerWithToken

from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from rest_framework import permissions,authentication, status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

    #     serializer.save(owner=self.request.user)
    
class Ekdilwsi2View(viewsets.ModelViewSet):    

        # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    serializer_class = EkdilwsiSerializer             # add this
    queryset = Ekdilwsi.objects.all() 

class InviteView(viewsets.ModelViewSet):    

    serializer_class = InviteSerializer             # add this
    queryset = Invite.objects.all()  


class partnersTypeView(viewsets.ModelViewSet):    

    serializer_class = partnersTypeSerializer             # add this
    queryset = partnersType.objects.all()  

class partnersView(viewsets.ModelViewSet):    

    serializer_class = partnersSerializer             # add this
    queryset = partners.objects.all()  

class libraryView(viewsets.ModelViewSet):    

    serializer_class = librarySerializer             # add this
    queryset = library.objects.all()  

class attendanceloggerView(viewsets.ModelViewSet):    

    serializer_class = attendanceloggerSerializer             # add this
    queryset = attendancelogger.objects.all()  


class GroupView(viewsets.ModelViewSet):
    serializer_class = GroupSerializer   
    queryset = Group.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer   
    queryset = User.objects.all()



class UserList(APIView):

    authentication_classes = (authentication.SessionAuthentication, authentication.BasicAuthentication, authentication.TokenAuthentication)
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # print("okkk")
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PermissionView(viewsets.ModelViewSet):
    serializer_class = PermissionSerializer   
    queryset = Permission.objects.all()    

@api_view(['GET'])
def current_user(request):
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
    









class EkdilwsiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data = request.data
        return Response(data, status=200)



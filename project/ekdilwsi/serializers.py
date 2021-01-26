from rest_framework import serializers


from .models import Ekdilwsi
from .models import Invite
from .models import partnersType
from .models import partners
from .models import library
from .models import attendancelogger



from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import Permission


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'   

class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)
    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.is_staff=True
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password','first_name', 'last_name', 'email')

class EkdilwsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ekdilwsi
        fields = ('id','name', 'description','info', 'place','happeningdate', 'organizer','partners','sponsors'
        ,'onetime','isfree','cost','venueneeded','costvenue','cateringneeded','costperperson')

      

class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ('id','ekdilwsiinvited','fromUser', 'toUser', 'sentdate','isopened', 'isAccepted','isRejected','isDeciding', 'info')

        
class partnersTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = partnersType
        fields = ('id','typename')

class partnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = partners
        fields = ('id','user','ptype', 'address','fblink','description', 'worklink',  'afm', 'cost','details')


      

class librarySerializer(serializers.ModelSerializer):
    class Meta:
        model = library
        fields = ('id','name','location')



class attendanceloggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendancelogger
        fields = ('id','first_name','last_name', 'email', 'credentials','libraryvisited', 'section','reason','timelogged')

        

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'        

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'        


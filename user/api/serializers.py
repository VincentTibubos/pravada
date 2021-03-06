from rest_framework.serializers import ModelSerializer
from user.models import Profile,Publication,Role

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class OrgSerializer(ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

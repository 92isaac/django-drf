from rest_framework.serializers import ModelSerializer
from .models import Developer

class DeveloperSerializer(ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'
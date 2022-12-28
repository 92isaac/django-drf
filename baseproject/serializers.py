from rest_framework.serializers import ModelSerializer
from .models import Developer, Company




class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DeveloperSerializer(ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Developer
        fields = '__all__'
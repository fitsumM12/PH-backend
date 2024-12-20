from rest_framework import serializers
from .models import usersDetail
from .models import DashboardProfile

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = usersDetail
        fields = '__all__'


# FOR UPDATING DASHBOARD PROFILE
from rest_framework import serializers
from .models import DashboardProfile

class DashboardProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardProfile
        fields = ['id', 'dashboard_image', 'landingpage_image', 'bio', 'updated_at']
        read_only_fields = ['updated_at']

    def update(self, instance, validated_data):
        # Only update fields if they are provided
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


from rest_framework import serializers
from .models import DashboardProfile

class LandingPageImageSerializer(serializers.ModelSerializer):
    landingpage_image = serializers.SerializerMethodField()

    class Meta:
        model = DashboardProfile
        fields = ['landingpage_image']

    def get_landingpage_image(self, obj):
        request = self.context.get('request')  
        if obj.landingpage_image:
            return request.build_absolute_uri(obj.landingpage_image.url)  
        return None


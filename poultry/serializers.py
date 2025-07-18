from rest_framework import serializers
from .models import *
# from .models import IndividualEggProduction

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class IndividualBirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualBird
        fields = '__all__'

class RequesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requester
        fields = '__all__'
class ChickenDistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChickenDistribution
        fields = '__all__'

class IndividualFeedWaterIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualFeedWaterIntake
        fields = '__all__'

class IndividualEggProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualEggProduction
        fields = '__all__'

class IndividualBodyweightSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualBodyWeight
        fields = '__all__'

class GroupBodyWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupBodyWeight
        fields = '__all__'

class GroupFeedWaterIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupFeedWaterIntake
        fields = '__all__'

class ChickenGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChickenGroup
        fields = '__all__'

class GroupDeathSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupDeath
        fields = '__all__'

class GroupCullingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCulling
        fields = '__all__'

class GroupReplacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupReplacement
        fields = '__all__'

class GroupVaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupVaccination
        fields = '__all__'

class IndividualDeathSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualDeath
        fields = '__all__'

class IndividualVaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualVaccination
        fields = '__all__'


class HatcheryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HatcheryRecord
        fields = '__all__'

class IncubationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncubationRecord  
        fields = '__all__'

class HatcherySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = HatcherySummary  
        fields = '__all__'


class GroupEggProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupEggProduction
        fields = '__all__'



# New serializer for group egg production for dashboard purpose 
class NewChickenGroupSerializer(serializers.ModelSerializer):
    house = serializers.CharField(source='house.house_number')  

    class Meta:
        model = ChickenGroup
        fields = ['id', 'house']   



class NewGroupEggProductionSerializer(serializers.ModelSerializer):
    chicken_group = NewChickenGroupSerializer()   

    class Meta:
        model = GroupEggProduction
        fields = '__all__'

# New serializer for individual egg production for dashboard purpose 


class BreedSerializerForDashboard(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'   

class IndividualBirdSerializerForDashboard(serializers.ModelSerializer):
    breed = BreedSerializerForDashboard()  

    class Meta:
        model = IndividualBird
        fields = '__all__'  

class IndividualEggProductionDashboardSerializer(serializers.ModelSerializer):
    bird = IndividualBirdSerializerForDashboard()  

    class Meta:
        model = IndividualEggProduction
        fields = '__all__'  


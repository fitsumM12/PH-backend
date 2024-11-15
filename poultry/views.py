# IMPORT LIBRARIES
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import AuthenticationFailed
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
import os
from django.http import JsonResponse
from django.db.models import Sum, Count

from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.db.models.functions import ExtractMonth, ExtractYear


# BREED BACKEND APIS
# ADD NEW BREED
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_breed_api(request):
    serializer = BreedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
# FETCH ALL BREEDS
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_breed_api(request):
    breeds = Breed.objects.all()
    serializer = BreedSerializer(breeds, many=True)
    return Response(serializer.data)
# DELETE BREED
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_breed_api(request, pk):
    breed = Breed.objects.get(pk=pk)
    breed.delete()
    return Response(status=204)
# FETCH SINGLE BREED
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_breed_api(request, pk):
    breed = Breed.objects.get(pk=pk)
    serializer = BreedSerializer(breed)
    return Response(serializer.data)
# UPDATE SINGLE BREED
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_breed_api(request, pk):
    breed = Breed.objects.get(pk=pk)
    serializer = BreedSerializer(breed, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# HOUSE BACKEND APIS
# ADD NEW HOUSE
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_house_api(request):
    serializer = HouseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
# FETCH ALL HOUSES
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_house_api(request):
    houses = House.objects.all()
    serializer = HouseSerializer(houses, many=True)
    return Response(serializer.data)
# DELETE HOUSE
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_house_api(request, pk):
    house = House.objects.get(pk=pk)
    house.delete()
    return Response(status=204)
# FETCH SINGLE HOUSE
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_house_api(request, pk):
    house = House.objects.get(pk=pk)
    serializer = HouseSerializer(house)
    return Response(serializer.data)
# UPDATE SINGLE HOUSE
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_house_api(request, pk):
    house = House.objects.get(pk=pk)
    serializer = HouseSerializer(house, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# CHICKEN BACKEND APIS
# ADD NEW CHICKEN
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_chicken_api(request):
    serializer = IndividualBirdSerializer(data=request.data)
    if serializer.is_valid():
        chicken = serializer.save()
        response_data = {
            'bird_id': chicken.bird_id,  
            **serializer.data       
        }
        return Response(response_data, status=201)
    return Response(serializer.errors, status=400)
# FETCH ALL CHICKEN
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_chicken_api(request):
    chickens = IndividualBird.objects.all()
    serializer = IndividualBirdSerializer(chickens, many=True)
    return Response(serializer.data)
# DELETE CHICKEN
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_chicken_api(request, pk):
    bird = IndividualBird.objects.get(pk=pk)
    bird.delete()
    return Response(status=204)
# FETCH SINGLE CHICKEN
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_chicken_api(request, pk):
    bird = IndividualBird.objects.get(pk=pk)
    serializer = IndividualBirdSerializer(bird)
    return Response(serializer.data)
# UPDATE SINGLE CHICKEN
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_chicken_api(request, pk):
    chicken = IndividualBird.objects.get(pk=pk)
    serializer = IndividualBirdSerializer(chicken, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# BODYWEIGHT BACKEND APIS
# ADD NEW BODYWEIGHT
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_bodyweight_api(request):
    serializer = IndividualBodyweightSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
# FETCH ALL BODYWEIGHT
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_bodyweight_api(request):
    chickens = IndividualBodyWeight.objects.all()
    serializer = IndividualBodyweightSerializer(chickens, many=True)
    return Response(serializer.data)
# DELETE BODY WEIGHT
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_bodyweight_api(request, pk):
    bird = IndividualBodyWeight.objects.get(pk=pk)
    bird.delete()
    return Response(status=204)
# FETCH SINGLE BODY WEIGHT
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_bodyweight_api(request, pk):
    bird = IndividualBodyWeight.objects.get(pk=pk)
    serializer = IndividualBodyweightSerializer(bird)
    return Response(serializer.data)
# UPDATE SINGLE BODYWEIGHT
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_bodyweight_api(request, pk):
    chicken = IndividualBodyWeight.objects.get(pk=pk)
    serializer = IndividualBodyweightSerializer(chicken, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

# INTAKE BACKEND APIS
# ADD NEW INTAKE
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_intake_api(request):
    serializer = IndividualFeedWaterIntakeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
# FETCH ALL INTAKE
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_intake_api(request):
    intakes = IndividualFeedWaterIntake.objects.all()
    serializer = IndividualFeedWaterIntakeSerializer(intakes, many=True)
    return Response(serializer.data)
# DELETE INTAKE
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_intake_api(request, pk):
    intake = IndividualFeedWaterIntake.objects.get(pk=pk)
    intake.delete()
    return Response(status=204)
# FETCH SINGLE INTAKE
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_intake_api(request, pk):
    intake = IndividualFeedWaterIntake.objects.get(pk=pk)
    serializer = IndividualFeedWaterIntakeSerializer(intake)
    return Response(serializer.data)
# UPDATE SINGLE INTAKE
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_intake_api(request, pk):
    intake = IndividualFeedWaterIntake.objects.get(pk=pk)
    serializer = IndividualFeedWaterIntakeSerializer(intake, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# EGG BACKEND APIS
# ADD NEW EGG
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_egg_api(request):
    serializer = IndividualEggProductionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
# FETCH ALL EGG
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_egg_api(request):
    eggs = IndividualEggProduction.objects.all()
    serializer = IndividualEggProductionSerializer(eggs, many=True)
    return Response(serializer.data)
# DELETE EGG
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_egg_api(request, pk):
    egg = IndividualEggProduction.objects.get(pk=pk)
    egg.delete()
    return Response(status=204)
# FETCH SINGLE EGG
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_egg_api(request, pk):
    egg = IndividualEggProduction.objects.get(pk=pk)
    serializer = IndividualEggProductionSerializer(egg)
    return Response(serializer.data)
# UPDATE SINGLE EGG
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_egg_api(request, pk):
    egg = IndividualEggProduction.objects.get(pk=pk)
    serializer = IndividualEggProductionSerializer(egg, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)



# GROUP CHICKEN BACKEND APIS
# ADD NEW GROUP CHICKEN
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_group_chicken_api(request):
    serializer = ChickenGroupSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
# FETCH ALL GROUP CHICKEN
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_group_chicken_api(request):
    chickens = ChickenGroup.objects.all()
    serializer = ChickenGroupSerializer(chickens, many=True)
    return Response(serializer.data)
# DELETE GROUP CHICKEN
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_group_chicken_api(request, pk):
    bird = ChickenGroup.objects.get(pk=pk)
    bird.delete()
    return Response(status=204)
# FETCH SINGLE GROUP CHICKEN
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_group_chicken_api(request, pk):
    bird = ChickenGroup.objects.get(pk=pk)
    serializer = ChickenGroupSerializer(bird)
    return Response(serializer.data)
# UPDATE SINGLE GROUP CHICKEN
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_group_chicken_api(request, pk):
    chicken = ChickenGroup.objects.get(pk=pk)
    serializer = ChickenGroupSerializer(chicken, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# BODYWEIGHT BACKEND APIS
# ADD NEW BODYWEIGHT
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_group_bodyweight_api(request):
    serializer = GroupBodyWeightSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
# FETCH ALL BODYWEIGHT
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_group_bodyweight_api(request):
    chickens = GroupBodyWeight.objects.all()
    serializer = GroupBodyWeightSerializer(chickens, many=True)
    return Response(serializer.data)
# DELETE BODY WEIGHT
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_group_bodyweight_api(request, pk):
    bird = GroupBodyWeight.objects.get(pk=pk)
    bird.delete()
    return Response(status=204)
# FETCH SINGLE BODY WEIGHT
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_group_bodyweight_api(request, pk):
    bird = GroupBodyWeight.objects.get(pk=pk)
    serializer = GroupBodyWeightSerializer(bird)
    return Response(serializer.data)
# UPDATE SINGLE BODYWEIGHT
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_group_bodyweight_api(request, pk):
    chicken = GroupBodyWeight.objects.get(pk=pk)
    serializer = GroupBodyWeightSerializer(chicken, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# GROUP BACKEND APIS
# ADD NEW GROUP INTAKE
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_group_intake_api(request):
    serializer = GroupFeedWaterIntakeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
# FETCH ALL GROUP INTAKE
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_group_intake_api(request):
    intakes = GroupFeedWaterIntake.objects.all()
    serializer = GroupFeedWaterIntakeSerializer(intakes, many=True)
    return Response(serializer.data)
# DELETE GROUP INTAKE
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_group_intake_api(request, pk):
    intake = GroupFeedWaterIntake.objects.get(pk=pk)
    intake.delete()
    return Response(status=204)
# FETCH SINGLE GROUPINTAKE
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_group_intake_api(request, pk):
    intake = GroupFeedWaterIntake.objects.get(pk=pk)
    serializer = GroupFeedWaterIntakeSerializer(intake)
    return Response(serializer.data)
# UPDATE SINGLE GROUP INTAKE
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_group_intake_api(request, pk):
    intake = GroupFeedWaterIntake.objects.get(pk=pk)
    serializer = GroupFeedWaterIntakeSerializer(intake, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# EGG BACKEND APIS
# ADD NEW EGG
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_group_egg_api(request):
    serializer = GroupEggProductionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
# FETCH ALL EGG
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_group_egg_api(request):
    eggs = GroupEggProduction.objects.all()
    serializer =GroupEggProductionSerializer(eggs, many=True)
    return Response(serializer.data)
# DELETE EGG
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_group_egg_api(request, pk):
    egg = GroupEggProduction.objects.get(pk=pk)
    egg.delete()
    return Response(status=204)
# FETCH SINGLE EGG
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_group_egg_api(request, pk):
    egg = GroupEggProduction.objects.get(pk=pk)
    serializer = GroupEggProductionSerializer(egg)
    return Response(serializer.data)

# UPDATE SINGLE EGG
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_group_egg_api(request, pk):
    egg = GroupEggProduction.objects.get(pk=pk)
    serializer = GroupEggProductionSerializer(egg, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
































# GROUP DEATH BACKEND APIS
# ADD NEW EGG
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_group_death_api(request):
    serializer = GroupDeathSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
# FETCH ALL DEATH
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_group_death_api(request):
    death = GroupDeath.objects.all()
    serializer =GroupDeathSerializer(death, many=True)
    return Response(serializer.data)
# DELETE DEATH
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_group_death_api(request, pk):
    death = GroupDeath.objects.get(pk=pk)
    death.delete()
    return Response(status=204)
# FETCH SINGLE DEATH
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_group_death_api(request, pk):
    death = GroupDeath.objects.get(pk=pk)
    serializer = GroupDeathSerializer(death)
    return Response(serializer.data)

# UPDATE SINGLE EGG
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_group_death_api(request, pk):
    death = GroupDeath.objects.get(pk=pk)
    serializer = GroupDeathSerializer(death, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)




# GROUP CULLING BACKEND APIS
# ADD NEW CULLING
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_group_culling_api(request):
    serializer = GroupCullingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# FETCH ALL CULLING
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_group_culling_api(request):
    culling = GroupCulling.objects.all()
    serializer =GroupCullingSerializer(culling, many=True)
    return Response(serializer.data)

# DELETE CULLING
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_group_culling_api(request, pk):
    culling = GroupCulling.objects.get(pk=pk)
    culling.delete()
    return Response(status=204)

# FETCH SINGLE CULLLING
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_group_culling_api(request, pk):
    culling = GroupCulling.objects.get(pk=pk)
    serializer = GroupCullingSerializer(culling)
    return Response(serializer.data)

# UPDATE SINGLE CULLING
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_group_culling_api(request, pk):
    culling = GroupCulling.objects.get(pk=pk)
    serializer = GroupCullingSerializer(culling, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# GROUP REPLACEMENT BACKEND APIS
# ADD NEW REPLACEMENT
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_group_replacement_api(request):
    serializer = GroupReplacementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# FETCH ALL REPLACEMENT
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_group_replacement_api(request):
    replace = GroupReplacement.objects.all()
    serializer =GroupReplacementSerializer(replace, many=True)
    return Response(serializer.data)

# DELETE REPLACEMENT
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_group_replacement_api(request, pk):
    replace = GroupReplacement.objects.get(pk=pk)
    replace.delete()
    return Response(status=204)

# FETCH SINGLE REPLACEMENT
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_group_replacement_api(request, pk):
    replace = GroupReplacement.objects.get(pk=pk)
    serializer = GroupReplacementSerializer(replace)
    return Response(serializer.data)

# UPDATE SINGLE REPLACEMENT
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_group_replacement_api(request, pk):
    replace = GroupReplacement.objects.get(pk=pk)
    serializer = GroupReplacementSerializer(replace, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)











# INDIVIDUAL DEATH BACKEND APIS
# ADD NEW DEATH
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_individual_death_api(request):
    serializer = IndividualDeathSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# FETCH ALL DEATH
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_individual_death_api(request):
    replace = IndividualDeath.objects.all()
    serializer =IndividualDeathSerializer(replace, many=True)
    return Response(serializer.data)

# DELETE DEATH
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_individual_death_api(request, pk):
    replace = IndividualDeath.objects.get(pk=pk)
    replace.delete()
    return Response(status=204)

# FETCH SINGLE DEATH
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_individual_death_api(request, pk):
    replace =IndividualDeath.objects.get(pk=pk)
    serializer = IndividualDeathSerializer(replace)
    return Response(serializer.data)

# UPDATE SINGLE DEATH
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_individual_death_api(request, pk):
    replace = IndividualDeath.objects.get(pk=pk)
    serializer = IndividualDeathSerializer(replace, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


















#  VACCINATION BACKEND APIS
# ADD NEW VACCINATION
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_group_vaccine_api(request):
    serializer = GroupVaccinationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# FETCH ALL VACCINATION
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_group_vaccine_api(request):
    replace = GroupVaccination.objects.all()
    serializer =GroupVaccinationSerializer(replace, many=True)
    return Response(serializer.data)

# DELETE VACCINATION
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_group_vaccine_api(request, pk):
    replace = GroupVaccination.objects.get(pk=pk)
    replace.delete()
    return Response(status=204)

# FETCH SINGLE VACCINATION
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_group_vaccine_api(request, pk):
    replace =GroupVaccination.objects.get(pk=pk)
    serializer = GroupVaccinationSerializer(replace)
    return Response(serializer.data)

# UPDATE SINGLE VACCINATION
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_group_vaccine_api(request, pk):
    replace = GroupVaccination.objects.get(pk=pk)
    serializer = GroupVaccinationSerializer(replace, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)






#  VACCINATION BACKEND APIS
# ADD NEW VACCINATION
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_individual_vaccine_api(request):
    serializer = IndividualVaccinationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# FETCH ALL VACCINATION
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_individual_vaccine_api(request):
    replace = IndividualVaccination.objects.all()
    serializer =IndividualVaccinationSerializer(replace, many=True)
    return Response(serializer.data)

# DELETE VACCINATION
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_individual_vaccine_api(request, pk):
    replace = IndividualVaccination.objects.get(pk=pk)
    replace.delete()
    return Response(status=204)

# FETCH SINGLE VACCINATION
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_individual_vaccine_api(request, pk):
    replace =IndividualVaccination.objects.get(pk=pk)
    serializer = IndividualVaccinationSerializer(replace)
    return Response(serializer.data)

# UPDATE SINGLE VACCINATION
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_individual_vaccine_api(request, pk):
    replace = IndividualVaccination.objects.get(pk=pk)
    serializer = IndividualVaccinationSerializer(replace, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)















#  HATCHERY RECORD BACKEND APIS
# ADD NEW HATCHERY RECORD
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_hatchery_record_api(request):
    serializer = HatcheryRecordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# FETCH ALL HATCHERY RECORD
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_hatchery_record_api(request):
    replace = HatcheryRecord.objects.all()
    serializer =HatcheryRecordSerializer(replace, many=True)
    return Response(serializer.data)

# DELETE HATCHERY RECORD
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_hatchery_record_api(request, pk):
    replace = HatcheryRecord.objects.get(pk=pk)
    replace.delete()
    return Response(status=204)

# FETCH SINGLE HATCHERY RECORD
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_hatchery_record_api(request, pk):
    replace =HatcheryRecord.objects.get(pk=pk)
    serializer = HatcheryRecordSerializer(replace)
    return Response(serializer.data)

# UPDATE SINGLE HATCHERY RECORD
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_hatchery_record_api(request, pk):
    replace = HatcheryRecord.objects.get(pk=pk)
    serializer = HatcheryRecordSerializer(replace, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)






# INCUBATION RECORD BACKEND APIS
# ADD NEW INCUBATION
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_incubation_record_api(request):
    serializer = IncubationRecordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# FETCH ALL INCUBATION
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_incubation_record_api(request):
    replace = IncubationRecord.objects.all()
    serializer =IncubationRecordSerializer(replace, many=True)
    return Response(serializer.data)

# DELETE INCUBATION
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_incubation_record_api(request, pk):
    replace = IncubationRecord.objects.get(pk=pk)
    replace.delete()
    return Response(status=204)

# FETCH SINGLE INCUBATION
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_incubation_record_api(request, pk):
    replace =IncubationRecord.objects.get(pk=pk)
    serializer = IncubationRecordSerializer(replace)
    return Response(serializer.data)

# UPDATE SINGLE INCUBATION
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_incubation_record_api(request, pk):
    replace = IncubationRecord.objects.get(pk=pk)
    serializer = IncubationRecordSerializer(replace, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)







# HATCHERY SUMMARY BACKEND APIS
# ADD NEW HATCHERY SUMMARY
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_hatchery_summary_api(request):
    serializer = HatcherySummarySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# FETCH ALL HATCHERY SUMMARY
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_hatchery_summary_api(request):
    replace = HatcherySummary.objects.all()
    serializer =HatcherySummarySerializer(replace, many=True)
    return Response(serializer.data)

# DELETE HATCHERY SUMMARY
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_hatchery_summary_api(request, pk):
    replace = HatcherySummary.objects.get(pk=pk)
    replace.delete()
    return Response(status=204)

# FETCH SINGLE HATCHERY SUMMARY
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_one_hatchery_summary_api(request, pk):
    replace =HatcherySummary.objects.get(pk=pk)
    serializer = HatcherySummarySerializer(replace)
    return Response(serializer.data)

# UPDATE SINGLE HATCHERY SUMMARY
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_hatchery_summary_api(request, pk):
    replace = HatcherySummary.objects.get(pk=pk)
    serializer = HatcherySummarySerializer(replace, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)










# FETCH TOTAL EGG PRODUCTION
# FETCH EGG PRODUCTION FOR EACH GROUP
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_egg_production_per_group_api(request):
    # Get all chicken groups
    groups = ChickenGroup.objects.all()
    
    egg_production_data = []

    for group in groups:
        total_production = (
            GroupEggProduction.objects
            .filter(chicken_group=group)
            .values(year=ExtractYear('collection_date'), month=ExtractMonth('collection_date')) 
            .annotate(total_eggs=Sum('total_egg_production'))
            .order_by('year', 'month')
        )

        house = group.house  
        house_number = house.house_number if house else "N/A"
        pen_number = house.pen_number if house else "N/A"
        for record in total_production:
            egg_production_data.append({
                "group_id": group.id,
                "house_number": house_number,
                "pen_number": pen_number,
                "year": record['year'],
                "month": record['month'],
                "total_egg_production": record['total_eggs'] or 0
            })

    return Response(egg_production_data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_feed_intake_refusal_per_group_api(request):
    groups = ChickenGroup.objects.all()
    
    feed_intake_data = []
    feed_refusal_data = []

    for group in groups:
        total_feed_intake = (
            GroupFeedWaterIntake.objects
            .filter(chicken_group=group)
            .values(year=ExtractYear('record_date'), month=ExtractMonth('record_date')) 
            .annotate(total_feed=Sum('feed_given'))
            .order_by('year', 'month')
        )

        total_feed_refusal = (
            GroupFeedWaterIntake.objects
            .filter(chicken_group=group)
            .values(year=ExtractYear('record_date'), month=ExtractMonth('record_date')) 
            .annotate(total_refusal=Sum('feed_refusal'))
            .order_by('year', 'month')
        )

        house = group.house  
        house_number = house.house_number if house else "N/A"
        pen_number = house.pen_number if house else "N/A"

        for record in total_feed_intake:
            feed_intake_data.append({
                "group_id": group.id,
                "house_number": house_number,
                "pen_number": pen_number,
                "year": record['year'],
                "month": record['month'],
                "total_feed_intake": record['total_feed'] or 0
            })

        for record in total_feed_refusal:
            feed_refusal_data.append({
                "group_id": group.id,
                "house_number": house_number,
                "pen_number": pen_number,
                "year": record['year'],
                "month": record['month'],
                "total_feed_refusal": record['total_refusal'] or 0
            })

    response_data = {
        "feed_intake": feed_intake_data,
        "feed_refusal": feed_refusal_data
    }

    return Response(response_data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_death_per_group_api(request):
    groups = ChickenGroup.objects.all()
    death_data = []
    for group in groups:
        total_deaths = (
            GroupDeath.objects
            .filter(chicken_group=group)
            .values(year=ExtractYear('date'), month=ExtractMonth('date')) 
            .annotate(
                total_male=Sum('male_count'),
                total_female=Sum('female_count'),
                total_death=Sum('total_count')
            )
            .order_by('year', 'month')
        )

        house = group.house  
        house_number = house.house_number if house else "N/A"
        pen_number = house.pen_number if house else "N/A"

        for record in total_deaths:
            death_data.append({
                "group_id": group.id,
                "house_number": house_number,
                "pen_number": pen_number,
                "year": record['year'],
                "month": record['month'],
                "total_male_deaths": record['total_male'] or 0,
                "total_female_deaths": record['total_female'] or 0,
                "total_deaths": record['total_death'] or 0
            })

    return Response(death_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_culling_per_group_api(request):
    groups = ChickenGroup.objects.all()
    
    culling_data = []

    for group in groups:
        total_culling = (
            GroupCulling.objects
            .filter(chicken_group=group)
            .values(year=ExtractYear('date'), month=ExtractMonth('date')) 
            .annotate(
                total_male=Sum('male_count'),
                total_female=Sum('female_count'),
                total_culling=Sum('total_count')
            )
            .order_by('year', 'month')
        )

        house = group.house  
        house_number = house.house_number if house else "N/A"
        pen_number = house.pen_number if house else "N/A"

        for record in total_culling:
            culling_data.append({
                "group_id": group.id,
                "house_number": house_number,
                "pen_number": pen_number,
                "year": record['year'],
                "month": record['month'],
                "total_male_cullings": record['total_male'] or 0,
                "total_female_cullings": record['total_female'] or 0,
                "total_cullings": record['total_culling'] or 0
            })

    return Response(culling_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_replacement_per_group_api(request):
    groups = ChickenGroup.objects.all()
    
    replacement_data = []

    for group in groups:
        total_replacements = (
            GroupReplacement.objects
            .filter(chicken_group=group)
            .values(year=ExtractYear('date'), month=ExtractMonth('date')) 
            .annotate(
                total_male=Sum('male_count'),
                total_female=Sum('female_count'),
                total_replacement=Sum('total_count')
            )
            .order_by('year', 'month')
        )

        house = group.house  
        house_number = house.house_number if house else "N/A"
        pen_number = house.pen_number if house else "N/A"

        for record in total_replacements:
            replacement_data.append({
                "group_id": group.id,
                "house_number": house_number,
                "pen_number": pen_number,
                "year": record['year'],
                "month": record['month'],
                "total_male_replacements": record['total_male'] or 0,
                "total_female_replacements": record['total_female'] or 0,
                "total_replacements": record['total_replacement'] or 0
            })

    return Response(replacement_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_body_weight_per_group_api(request):
    groups = ChickenGroup.objects.all()
    
    body_weight_data = []

    for group in groups:
        total_body_weight = (
            GroupBodyWeight.objects
            .filter(chicken_group=group)
            .values(year=ExtractYear('record_date'), month=ExtractMonth('record_date')) 
            .annotate(
                total_weight=Sum('total_weight')
            )
            .order_by('year', 'month')
        )

        house = group.house  
        house_number = house.house_number if house else "N/A"
        pen_number = house.pen_number if house else "N/A"

        for record in total_body_weight:
            body_weight_data.append({
                "group_id": group.id,
                "house_number": house_number,
                "pen_number": pen_number,
                "year": record['year'],
                "month": record['month'],
                "total_body_weight": record['total_weight'] or 0.0
            })

    return Response(body_weight_data)





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_vaccination_count_per_group_api(request):
    groups = ChickenGroup.objects.all()
    
    vaccination_data = []

    for group in groups:
        total_vaccinations = (
            GroupVaccination.objects
            .filter(chicken_group=group)
            .annotate(
                year=ExtractYear('date'),
                month=ExtractMonth('date')
            )
            .values('year', 'month')
            .annotate(vaccination_count=Count('id'))  # Count each record
            .order_by('year', 'month')
        )

        house_number = group.house.house_number if group.house else "N/A"
        pen_number = group.house.pen_number if group.house else "N/A"

        for record in total_vaccinations:
            vaccination_data.append({
                "group_id": group.id,
                "house_number": house_number,
                "pen_number": pen_number,
                "year": record['year'],
                "month": record['month'],
                "vaccination_count": record['vaccination_count']
            })

    return Response(vaccination_data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def count_chicken_groups_api(request):
    group_count = ChickenGroup.objects.count()
    return Response({"total_chicken_groups": group_count})

# Monthly Egg Production
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_egg_production_per_individual_chicken_api(request):
    chickens = IndividualBird.objects.all()
    egg_production_data = []

    for chicken in chickens:
        total_production = (
            IndividualEggProduction.objects
            .filter(bird=chicken)
            .values(year=ExtractYear('date'), month=ExtractMonth('date'))
            .annotate(egg_count=Sum('egg_count'))
            .order_by('year', 'month')
        )

        # Access house and pen numbers
        house = chicken.house  
        house_number = house.house_number if house else "N/A"
        pen_number = house.pen_number if house else "N/A"
        
        for record in total_production:
            egg_production_data.append({
                "id": chicken.id,
                "chicken_id": chicken.bird_id,
                "house_number": house_number, 
                "pen_number": pen_number,     
                "year": record['year'],
                "month": record['month'],
                "total_egg_production": record['egg_count'] or 0
            })

    return Response(egg_production_data)

# Monthly Feed Intake and Refusal
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_feed_intake_refusal_per_individual_chicken_api(request):
    chickens = IndividualBird.objects.all()
    feed_intake_data = []
    feed_refusal_data = []

    for chicken in chickens:
        # Use 'bird' instead of 'individual_chicken'
        total_feed_intake = (
            IndividualFeedWaterIntake.objects
            .filter(bird=chicken)  # Corrected to use 'bird'
            .values(year=ExtractYear('record_date'), month=ExtractMonth('record_date'))
            .annotate(total_feed=Sum('feed_given'))
            .order_by('year', 'month')
        )

        total_feed_refusal = (
            IndividualFeedWaterIntake.objects
            .filter(bird=chicken)  # Corrected to use 'bird'
            .values(year=ExtractYear('record_date'), month=ExtractMonth('record_date'))
            .annotate(total_refusal=Sum('feed_refusal'))
            .order_by('year', 'month')
        )

        house = chicken.house  
        house_number = house.house_number if house else "N/A"
        pen_number = house.pen_number if house else "N/A"

        for record in total_feed_intake:
            feed_intake_data.append({
                "chicken_id": chicken.id,
                "house_number": house_number, 
                "pen_number": pen_number,     
                "year": record['year'],
                "month": record['month'],
                "total_feed_intake": record['total_feed'] or 0
            })

        for record in total_feed_refusal:
            feed_refusal_data.append({
                "chicken_id": chicken.id,
                "house_number": house_number, 
                "pen_number": pen_number,     
                "year": record['year'],
                "month": record['month'],
                "total_feed_refusal": record['total_refusal'] or 0
            })

    return Response({
        "feed_intake": feed_intake_data,
        "feed_refusal": feed_refusal_data
    })
# Monthly Body Weight
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_body_weight_per_individual_chicken_api(request):
    chickens = IndividualBird.objects.all()
    body_weight_data = []

    for chicken in chickens:
        total_body_weight = (
            IndividualBodyWeight.objects
            .filter(bird=chicken)
            .values(year=ExtractYear('record_date'), month=ExtractMonth('record_date'))
            .annotate(average_weight=Sum('weight') / Count('weight')) 
            .order_by('year', 'month')
        )

        house = chicken.house  
        house_number = house.house_number if house else "N/A"
        pen_number = house.pen_number if house else "N/A"

        for record in total_body_weight:
            body_weight_data.append({
                "id":chicken.id,
                "chicken_id": chicken.bird_id,
                "house_number": house_number, 
                "pen_number": pen_number,     
                "year": record['year'],
                "month": record['month'],
                "average_body_weight": record['average_weight'] or 0
            })

    return Response(body_weight_data)

# Monthly Vaccination Count
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_vaccination_count_per_individual_chicken_api(request):
    chickens = IndividualBird.objects.all()
    vaccination_data = []

    for chicken in chickens:
        total_vaccinations = (
            IndividualVaccination.objects
            .filter(bird=chicken)
            .values(year=ExtractYear('date'), month=ExtractMonth('date'))
            .annotate(total_vaccines=Count('vaccine_type')) 
            .order_by('year', 'month')
        )

        house = chicken.house  
        house_number = house.house_number if house else "N/A"
        pen_number = house.pen_number if house else "N/A"

        for record in total_vaccinations:
            vaccination_data.append({
                "id": chicken.id,
                "chicken_id": chicken.bird_id,
                "house_number": house_number, 
                "pen_number": pen_number,     
                "year": record['year'],
                "month": record['month'],
                "total_vaccinations": record['total_vaccines'] or 0
            })

    return Response(vaccination_data)

# Count Individual Chickens
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def count_individual_chickens_api(request):
    total_chickens = IndividualBird.objects.count()
    return Response({"total_individual_chickens": total_chickens})

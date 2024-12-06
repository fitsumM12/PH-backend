from django.db.models import Sum
from .models import ChickenGroup, GroupCulling

def validate_operation(chicken_group, operation_type, male_count, female_count):
    """
    Validates whether an operation (e.g., culling, mortality) can be performed on a ChickenGroup.

    Args:
        chicken_group_id (int): The ID of the ChickenGroup.
        operation_type (str): The type of operation (e.g., "culling", "mortality").
        male_count (int): The number of male chickens involved in the operation.
        female_count (int): The number of female chickens involved in the operation.

    Returns:
        dict: Validation status and available chickens.
    """
    # Ensure male_count and female_count are integers
    male_count = int(male_count)
    female_count = int(female_count)

    chicken_group = ChickenGroup.objects.get(id=chicken_group)
    original_male_count = chicken_group.male_count
    original_female_count = chicken_group.female_count

    # Calculate already affected chickens based on operation type
    if operation_type == "culling":
        records = GroupCulling.objects.filter(chicken_group=chicken_group)
    elif operation_type == "mortality":
        # Add logic for mortality records here
        records = []  # Replace with actual mortality model query
    elif operation_type == "replacement":
        # Add logic for replacement records here
        records = []  # Replace with actual replacement model query
    else:
        raise ValueError("Invalid operation type")

    total_male_affected = records.aggregate(Sum('male_count'))['male_count__sum'] or 0
    total_female_affected = records.aggregate(Sum('female_count'))['female_count__sum'] or 0

    # Available chickens
    available_male = original_male_count - total_male_affected
    available_female = original_female_count - total_female_affected

    # Validate counts
    if male_count > available_male or female_count > available_female:
        validation_result = {
            "status": False,
            "message": "Operation exceeds available chickens",
            "available_male": available_male,
            "available_female": available_female,
        }
        print(validation_result)  # Log validation result to the console
        return validation_result
    
    validation_result = {"status": True, "available_male": available_male, "available_female": available_female}
    print(validation_result)  # Log validation result to the console
    return validation_result

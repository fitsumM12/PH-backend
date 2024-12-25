from django.db.models import Sum
from .models import ChickenGroup, GroupCulling, GroupDeath, GroupReplacement

def validate_operation(chicken_group_id, operation_type, male_count, female_count):
    """
    Validates whether an operation (e.g., culling, mortality, replacement) can be performed on a ChickenGroup.

    Args:
        chicken_group_id (int): The ID of the ChickenGroup.
        operation_type (str): The type of operation (e.g., "culling", "mortality", "replacement").
        male_count (int): The number of male chickens involved in the operation.
        female_count (int): The number of female chickens involved in the operation.

    Returns:
        dict: Validation status and available chickens.
    """
    # Ensure male_count and female_count are integers
    male_count = int(male_count)
    female_count = int(female_count)

    chicken_group = ChickenGroup.objects.get(id=chicken_group_id)
    original_male_count = chicken_group.male_count
    original_female_count = chicken_group.female_count

    # Sum all affected chickens for each operation
    culling_records = GroupCulling.objects.filter(chicken_group=chicken_group)
    mortality_records = GroupDeath.objects.filter(chicken_group=chicken_group)
    replacement_records = GroupReplacement.objects.filter(chicken_group=chicken_group)

    total_male_culled = culling_records.aggregate(Sum('male_count'))['male_count__sum'] or 0
    total_female_culled = culling_records.aggregate(Sum('female_count'))['female_count__sum'] or 0
    total_male_dead = mortality_records.aggregate(Sum('male_count'))['male_count__sum'] or 0
    total_female_dead = mortality_records.aggregate(Sum('female_count'))['female_count__sum'] or 0
    total_male_replaced = replacement_records.aggregate(Sum('male_count'))['male_count__sum'] or 0
    total_female_replaced = replacement_records.aggregate(Sum('female_count'))['female_count__sum'] or 0

    available_male = original_male_count - total_male_culled - total_male_dead + total_male_replaced
    available_female = original_female_count - total_female_culled - total_female_dead + total_female_replaced

    # Ensure replacements are only done if there's prior culling or mortality
    if operation_type == "replacement":
        if (total_male_culled + total_male_dead) == 0 and (total_female_culled + total_female_dead) == 0:
            validation_result = {
                "status": False,
                "message": "Replacements cannot be done without prior culling or mortality operations",
                "available_male": available_male,
                "available_female": available_female,
            }
            print(validation_result)  # Log validation result to the console
            return validation_result
        
        if male_count > (total_male_culled + total_male_dead) or female_count > (total_female_culled + total_female_dead):
            validation_result = {
                "status": False,
                "message": "Replacement exceeds the total of previous culling and mortality operations",
                "available_male": available_male,
                "available_female": available_female,
            }
            print(validation_result)  # Log validation result to the console
            return validation_result
    # Validate counts for culling and mortality
    if operation_type in ["culling", "mortality"]:
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

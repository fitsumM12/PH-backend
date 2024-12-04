from django.contrib import admin
from .models import (
    Breed,
    House,
    IndividualBird,
    IndividualEggProduction,
    IndividualFeedWaterIntake,
    IndividualBodyWeight,
    ChickenGroup,
    GroupBodyWeight,
    GroupEggProduction,
    GroupFeedWaterIntake,
    GroupCulling,
    GroupDeath,
    GroupReplacement,
    GroupVaccination,
    IndividualVaccination,
    HatcheryRecord,
    HatcherySummary,
    IncubationRecord,
    Requester,
    ChickenDistribution
)

admin.site.register(Breed)
admin.site.register(House)
admin.site.register(IndividualBird)
admin.site.register(Requester)
admin.site.register(ChickenDistribution)
admin.site.register(IndividualEggProduction)
admin.site.register(IndividualFeedWaterIntake)
admin.site.register(IndividualBodyWeight)
admin.site.register(ChickenGroup)
admin.site.register(GroupBodyWeight)
admin.site.register(GroupEggProduction)
admin.site.register(GroupFeedWaterIntake)
admin.site.register(GroupReplacement)
admin.site.register(GroupDeath)
admin.site.register(GroupVaccination)
admin.site.register(GroupCulling)
admin.site.register(IndividualVaccination)
admin.site.register(HatcheryRecord)
admin.site.register(HatcherySummary)
admin.site.register(IncubationRecord)



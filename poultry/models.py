from django.db import models
from usersDetail.models import usersDetail

# BREED
class Breed(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            existing_ids = list(Breed.objects.values_list('id', flat=True))
            new_id = 1
            while new_id in existing_ids:
                new_id += 1
            self.id = new_id  
        super(Breed, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# HOUSE
class House(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    house_number = models.CharField(max_length=50)
    pen_number = models.CharField(max_length=50)
    capacity = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            existing_ids = list(House.objects.values_list('id', flat=True))
            new_id = 1
            while new_id in existing_ids:
                new_id += 1
            self.id = new_id  
        super(House, self).save(*args, **kwargs)

    def __str__(self):
        return f"House {self.house_number}, Pen {self.pen_number}"

# INDIVIDUAL BIRD
class IndividualBird(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    bird_id = models.CharField(max_length=200, null=True, blank=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    date_of_hatch = models.DateField()
    point_of_lay_date = models.DateField(null=True, blank=True)
    generation = models.IntegerField()
    hatch = models.CharField(max_length=100)
    annotator = models.ForeignKey(usersDetail, on_delete=models.CASCADE)
    sire_id = models.CharField(max_length=300, null=True, blank=True)
    dam_id = models.CharField(max_length=200, null=True, blank=True)
    sex = models.CharField(max_length=10)
    remarks = models.TextField(null=True, blank=True)
    def save(self, *args, **kwargs):
            if not self.bird_id:
                existing_ids = list(IndividualBird.objects.values_list('id', flat=True))
                new_id = 1
                while new_id in existing_ids:
                    new_id += 1
                self.bird_id = new_id  
            super(IndividualBird, self).save(*args, **kwargs)
    def __str__(self):
        return f"Bird {self.bird_id}"

#  REQUESTER 
class Requester(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    requester_id = models.CharField(max_length=200, null=True, blank=True)
    requester_name = models.CharField(max_length=200, help_text="Name of the recipient")
    requester_region = models.CharField(max_length=200)
    requester_district = models.CharField(max_length=200)
    requester_city = models.CharField(max_length=200)
    requester_phone_number = models.CharField(max_length=15)
    requester_male_count = models.PositiveIntegerField(default=0)
    requester_female_count = models.PositiveIntegerField(default=0)
    def save(self, *args, **kwargs):
            if not self.requester_id:
                existing_ids = list(IndividualBird.objects.values_list('id', flat=True))
                new_id = 1
                while new_id in existing_ids:
                    new_id += 1
                self.requester = new_id  
            super(Requester, self).save(*args, **kwargs)
    def __str__(self):
        return f"Requester {self.requester_id}"

# CHICKEN DISTRIBUTION
class ChickenDistribution(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    chicken_distribution_id = models.CharField(max_length=200, null=True, blank=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    date_of_hatch = models.DateField()
    number_of_eggs_incubated = models.PositiveIntegerField(default=0)
    healthy_hatchlings_count = models.PositiveIntegerField(default=0) 
    requester = models.ForeignKey(Requester, on_delete = models.CASCADE)
    quantity_sold = models.PositiveIntegerField()
    distributor_name = models.ForeignKey(usersDetail, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
            if not self.chicken_distribution_id:
                existing_ids = list(ChickenDistribution.objects.values_list('id', flat=True))
                new_id = 1
                while new_id in existing_ids:
                    new_id += 1
                self.chicken_distribution_id = new_id  
            super(ChickenDistribution, self).save(*args, **kwargs)
    def __str__(self):
        return f"Distribution {self.chicken_distribution_id}"

# INDIVIDUAL DEATH
class IndividualDeath(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    bird = models.ForeignKey(IndividualBird, on_delete=models.CASCADE)
    date = models.DateField()
    condition = models.CharField(max_length=200, default="alive")
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)
    def save(self, *args, **kwargs):
            if not self.id:
                existing_ids = list(IndividualDeath.objects.values_list('id', flat=True))
                new_id = 1
                while new_id in existing_ids:
                    new_id += 1
                self.id = new_id  
            super(IndividualDeath, self).save(*args, **kwargs)
    def __str__(self):
        return f"Death for Bird {self.bird.bird_id} on {self.date}"
    

# INDIVIDUAL VACCINATION
class IndividualVaccination(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    bird = models.ForeignKey(IndividualBird, on_delete=models.CASCADE)
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    disease_type = models.CharField(max_length=255, null=True, blank=True)
    vaccine_type = models.CharField(max_length=255, null=True, blank=True)
    vaccine_method = models.CharField(max_length=255, null=True, blank=True)
    remark = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Vaccinations for Group {self.id} on {self.date}"

# INDIVIDUAL EGG PRODUCTION
class IndividualEggProduction(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    bird = models.ForeignKey(IndividualBird, on_delete=models.CASCADE)
    date = models.DateField()
    egg_count = models.IntegerField()
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
            if not self.id:
                existing_ids = list(IndividualEggProduction.objects.values_list('id', flat=True))
                new_id = 1
                while new_id in existing_ids:
                    new_id += 1
                self.id = new_id  
            super(IndividualEggProduction, self).save(*args, **kwargs)
    def __str__(self):
        return f"Egg production for Bird {self.bird.bird_id} on {self.date}"


# INDIVIDUAL FEED WATER INTAKE
class IndividualFeedWaterIntake(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    bird = models.ForeignKey(IndividualBird, on_delete=models.CASCADE)
    record_date = models.DateField()
    feed_given = models.FloatField()
    feed_refusal = models.FloatField(null=True, blank=True)
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE)
    remarks = models.TextField(null=True, blank=True)
    def save(self, *args, **kwargs):
            if not self.id:
                existing_ids = list(IndividualFeedWaterIntake.objects.values_list('id', flat=True))
                new_id = 1
                while new_id in existing_ids:
                    new_id += 1
                self.id = new_id  
            super(IndividualFeedWaterIntake, self).save(*args, **kwargs)
    def __str__(self):
        return f"Feed and Water Intake for Bird {self.id} on {self.record_date}"


# INDIVIDUAL BODYWEIGHT
class IndividualBodyWeight(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    bird = models.ForeignKey(IndividualBird, on_delete=models.CASCADE)
    record_date = models.DateField()
    weight = models.FloatField()
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE)
    remarks = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            existing_ids = list(IndividualBodyWeight.objects.values_list('id', flat=True))
            new_id = 1
            while new_id in existing_ids:
                new_id += 1
            self.id = new_id  
        super(IndividualBodyWeight, self).save(*args, **kwargs)
    def __str__(self):
        return f"Body Weight for Bird {self.id} on {self.record_date}"
    

# GROUP CHICKEN
class ChickenGroup(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE)
    date_of_hatch = models.DateField()
    point_of_lay_date = models.DateField(null=True, blank=True)
    female_count = models.IntegerField()
    male_count = models.IntegerField()
    total_bird_count = models.IntegerField()

    def save(self, *args, **kwargs):
        self.total_bird_count = self.male_count + self.female_count
        if not self.id:
            existing_ids = list(ChickenGroup.objects.values_list('id', flat=True))
            new_id = 1
            while new_id in existing_ids:
                new_id += 1
            self.id = new_id  
        super(ChickenGroup, self).save(*args, **kwargs)

    def __str__(self):
        return f"Chicken Group {self.id} (House: {self.house.house_number}, Breed: {self.breed.name})"

# GROUP CULLING
class GroupCulling(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    chicken_group = models.ForeignKey(ChickenGroup, on_delete=models.CASCADE)
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    reason = models.CharField(max_length=255, null=True, blank=True)
    male_count = models.IntegerField(default=0)
    female_count = models.IntegerField(default=0)
    total_count = models.IntegerField()

    def save(self, *args, **kwargs):
        self.total_count = self.male_count + self.female_count
        super(GroupCulling, self).save(*args, **kwargs)

    def __str__(self):
        return f"Culling Event for Group {self.id} on {self.date}"

# GROUP REPLACEMENT
class GroupReplacement(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    chicken_group = models.ForeignKey(ChickenGroup, on_delete=models.CASCADE)
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    male_count = models.IntegerField(default=0)
    female_count = models.IntegerField(default=0)
    total_count = models.IntegerField()

    def save(self, *args, **kwargs):
        self.total_count = self.male_count + self.female_count
        super(GroupReplacement, self).save(*args, **kwargs)

    def __str__(self):
        return f"Replacement Event for Group {self.id} on {self.date}"

     






# GROUP VACCINATION
class GroupVaccination(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    chicken_group = models.ForeignKey(ChickenGroup, on_delete=models.CASCADE)
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    disease_type = models.CharField(max_length=255, null=True, blank=True)
    vaccine_type = models.CharField(max_length=255, null=True, blank=True)
    vaccine_method = models.CharField(max_length=255, null=True, blank=True)
    remark = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Vaccinations for Group {self.id} on {self.date}"



# GROUP DEATH
class GroupDeath(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    chicken_group = models.ForeignKey(ChickenGroup, on_delete=models.CASCADE)
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE, default=1)
    date = models.DateField()
    reason = models.CharField(max_length=255, null=True, blank=True)
    male_count = models.IntegerField(default=0)
    female_count = models.IntegerField(default=0)
    total_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.total_count = self.male_count + self.female_count
        super(GroupDeath, self).save(*args, **kwargs)

    def __str__(self):
        return f"Death Event for Group {self.id} on {self.date}"

# GROUP BODY WEIGHT
class GroupBodyWeight(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    chicken_group = models.ForeignKey(ChickenGroup, on_delete=models.CASCADE)
    record_date = models.DateField()
    age_in_weeks = models.IntegerField()
    total_birds_weighted = models.IntegerField()
    total_weight = models.FloatField()
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE)
    remarks = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            existing_ids = list(GroupBodyWeight.objects.values_list('id', flat=True))
            new_id = 1
            while new_id in existing_ids:
                new_id += 1
            self.id = new_id  
        super(GroupBodyWeight, self).save(*args, **kwargs)

    def __str__(self):
        return f"Group Body Weight on {self.record_date}"

# GROUP EGG PRODUCTION 
class GroupEggProduction(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    chicken_group = models.ForeignKey(ChickenGroup, on_delete=models.CASCADE)
    collection_date = models.DateField()
    morning_egg_production = models.IntegerField()
    afternoon_egg_production = models.IntegerField()
    total_egg_production = models.IntegerField()
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE)
    remarks = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total_egg_production = self.morning_egg_production + self.afternoon_egg_production
        if not self.id:
            existing_ids = list(GroupEggProduction.objects.values_list('id', flat=True))
            new_id = 1
            while new_id in existing_ids:
                new_id += 1
            self.id = new_id  
        super(GroupEggProduction, self).save(*args, **kwargs)

    def __str__(self):
        return f"Group Egg Production on {self.collection_date}"

# GROUP FEED WATER INTAKE
class GroupFeedWaterIntake(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    chicken_group = models.ForeignKey(ChickenGroup, on_delete=models.CASCADE)
    record_date = models.DateField()
    feed_given = models.FloatField()
    feed_refusal = models.FloatField(null=True, blank=True)
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE)
    remarks = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            existing_ids = list(GroupFeedWaterIntake.objects.values_list('id', flat=True))
            new_id = 1
            while new_id in existing_ids:
                new_id += 1
            self.id = new_id  
        super(GroupFeedWaterIntake, self).save(*args, **kwargs)

    def __str__(self):
        return f"Feed and Water Intake on {self.record_date}"
    

class HatcheryRecord(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    breed_of_chicken = models.ForeignKey(Breed, on_delete=models.CASCADE)
    number_of_eggs_set = models.PositiveIntegerField()
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE, default=1)
    date_of_set = models.DateField()
    hour_of_set = models.TimeField()
    date_of_candling = models.DateField(null=True, blank=True)
    date_of_transfer = models.DateField(null=True, blank=True)
    def save(self, *args, **kwargs):
            if not self.id:
                existing_ids = list(HatcheryRecord.objects.values_list('id', flat=True))
                new_id = 1
                while new_id in existing_ids:
                    new_id += 1
                self.id = new_id  
            super(HatcheryRecord, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"Hatchery Unit {self.id} on {self.date_of_set}"

class IncubationRecord(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    hatchery_record = models.ForeignKey(HatcheryRecord, on_delete=models.CASCADE, related_name="incubation_records")
    day = models.PositiveIntegerField()
    incubation_set_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    egg_shell_temp_min = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    egg_shell_temp_med = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    egg_shell_temp_max = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    humidity_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    co2_level = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE, default=1)
    valve_status = models.CharField(max_length=50, null=True, blank=True)
    turning = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField()

    def save(self, *args, **kwargs):
            if not self.id:
                existing_ids = list(IncubationRecord.objects.values_list('id', flat=True))
                new_id = 1
                while new_id in existing_ids:
                    new_id += 1
                self.id = new_id  
            super(IncubationRecord, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"Incubation Unit {self.id} on {self.date}"

class HatcherySummary(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    hatchery_record = models.OneToOneField(HatcheryRecord, on_delete=models.CASCADE, related_name="summary")
    breed_of_chicken = models.ForeignKey(Breed, on_delete=models.CASCADE, default=1)
    number_set = models.PositiveIntegerField()
    total_infertile_eggs = models.PositiveIntegerField()
    total_hatched = models.PositiveIntegerField()
    hatch_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    collector = models.ForeignKey(usersDetail, on_delete=models.CASCADE, default=1)
    infertile_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    place_of_distribution = models.CharField(max_length=200, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
            if not self.id:
                existing_ids = list(HatcherySummary.objects.values_list('id', flat=True))
                new_id = 1
                while new_id in existing_ids:
                    new_id += 1
                self.id = new_id  
            super(HatcherySummary, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"Hatchery Unit {self.id} on {self.total_hatched}"
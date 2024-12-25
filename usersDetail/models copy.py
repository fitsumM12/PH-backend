from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class usersDetail(AbstractUser):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('BLOCKED', 'Blocked')
    ]

    ROLE_CHOICES = [
        ('SUPER ADMIN', 'Super Admin'),
        ('ADMIN', 'Admin'),
        ('USER', 'User')
    ]
    username = models.CharField(max_length=200, blank=False, unique=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=110, blank=True, null=True, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    zone = models.CharField(max_length=100, blank=True, null=True)
    kebele = models.CharField(max_length=100, blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=12, blank=True, null=True, choices=STATUS_CHOICES)
    role = models.CharField(max_length=110, blank=True, null=True, choices=ROLE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.username

# FOR UPDATING DASHBOARD PROFILE 
 
class DashboardProfile(models.Model):
    dashboard_image = models.ImageField(upload_to='dashboard_profiles/', null=True, blank=True)
    landingpage_image = models.ImageField(upload_to='landingpage_profiles/', null=True, blank=True)  # New field
    bio = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dashboard Profile {self.id}"

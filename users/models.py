from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomBaseManager

# Create your models here.
class CustomUser(AbstractUser):
    """
        Inherited from django abstract user model
    """

    # Stored in database as 'M' or 'F'
    GENDER_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE')
    ]
    # Same here
    STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('W', 'Widowed')
    ]

    username = None # default from AbstractUser change to None
    # Required Fields (On form)
    email = models.EmailField(unique = True) # R
    date_of_birth = models.DateField(blank = True, null = True) # R
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES) # R
    status = models.CharField(max_length = 1, choices = STATUS_CHOICES) # R 
    address = models.CharField(max_length = 200) # R
    city = models.CharField(max_length = 100) # R
    state = models.CharField(max_length = 100) # R
    country = models.CharField(max_length = 100) # R
    phone = models.CharField(max_length = 20, null = True) # R
    # Not Required Fields (On form)
    zip_code = models.IntegerField(null = True) # N
    profile = models.ImageField(upload_to='profile/', default="profile/profile_default.png", blank = True, null = True) # N
    middle_name = models.CharField(max_length = 50, null = True) # N
    height = models.IntegerField(null = True) # N
    weight = models.IntegerField(null = True) # N
    religion = models.CharField(max_length = 100, null = True) # N
    mother_name = models.CharField(max_length = 150, null = True)
    father_name = models.CharField(max_length = 150, null = True)
    mother_occupation = models.CharField(max_length = 100, null = True)
    father_occupation = models.CharField(max_length = 100, null = True)
    spouse_name = models.CharField(max_length = 150, null = True)
    spouse_occupation = models.CharField(max_length = 100, null = True)

    # Fields from the AbstractUser class
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender']

    objects = CustomBaseManager()

    # From the 'select' query you can get this values
    @property
    def name_formal(self):
        middle = self.middle_name[0] + '.' if self.middle_name is not None else ''
        return ''.join([self.last_name, ', ', self.first_name, ' ', middle])

    @property
    def name_casual(self):
        middle = self.middle_name[0] + '. ' if self.middle_name is not None else ''
        return ''.join([self.first_name, ' ', middle, self.last_name])

    @property
    def age(self):
        age = int((date.today() - self.date_of_birth).days / 365.2425)
        return age

    @property
    def full_address(self):
        return ''.join([self.address, ', ', self.state, ', ', self.city, ', ', self.country, ' ', str(self.zip_code)])

    def __str__(self):
        return self.email

    class Meta:
        db_table = "User"
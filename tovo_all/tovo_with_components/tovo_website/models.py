from email import message
from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class contact_us(models.Model):
    user_name = models.CharField(max_length=50,null=False)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    user_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list

    user_email = models.EmailField(max_length=254)
    user_message = models.TextField()

    def __str__(self):
        return self.user_name   

class subscription(models.Model):

    email = models.EmailField(max_length=254)
    subscribed = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email
    
from django.db import models

# Create your models here.
class Monkey(models.Model):
    
    # first_name VARCHAR(255)
    first_name = models.CharField(max_length=255)
    # last_name
    last_name = models.CharField(max_length=255)
    # email
    email = models.EmailField(unique=True)
    # phonenumber
    phone_number = models.IntegerField()
    password = models.CharField(max_length=255)


    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return "Monkey: {}".format(self.first_name)
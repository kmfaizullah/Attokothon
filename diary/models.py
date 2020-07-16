from django.db import models

# Create your models here.

"""
    Here, All the database schemas definition has been defined.
    Using this definition physical data schemas will be created in postgre sql database.
    After defining this model following steps will be required to create pysical databse.
    step 1 : execute 'python manage.py makemigrations diary' command. This will create a migration folder with 
             a python file look like 0001_initial.py
    step 2 : now execute 'python manage.py sqlmigrate diary 0001' command.
    step 3 : finally execute 'python manage.py migrate' command to create physical data.
"""
# difining sigup schemas
# There is no foriegn keys
# promary key will be automatically defined by system.
class Signup(models.Model):
    first_name = models.CharField(max_length=15)
    last_name  = models.CharField(max_length=15)
    user_name  = models.CharField(max_length=15)
    password  = models.CharField(max_length=15)
    mobile  = models.CharField(max_length=15)

# this class is for blog databse schema
class blog(models.Model):
    title = models.CharField(max_length=150)
    post  = models.CharField(max_length=5000)
    date  = models.CharField(max_length=15)

# this class definition is for bestplace schema
class bestPlace(models.Model):
    title = models.CharField(max_length=150)
    post  = models.CharField(max_length=5000)
    date  = models.CharField(max_length=15)
    keypoints  = models.CharField(max_length=1000)

# this class definition is for the momorabale journey schema
class memory(models.Model):
    title = models.CharField(max_length=150)
    post  = models.CharField(max_length=5000)
    date  = models.CharField(max_length=15)
    note  = models.CharField(max_length=1000)

# this class definition is for doto table schema
class todo(models.Model):
    task = models.CharField(max_length=150)
    place  = models.CharField(max_length=5000)
    date  = models.CharField(max_length=15)
    note  = models.CharField(max_length=1000)
    

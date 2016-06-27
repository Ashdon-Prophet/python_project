from __future__ import unicode_literals
import bcrypt
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]*$')
# custom manager to easily allow us to call methods that are specific to this project (e.g. login and register)
class UserManager(models.Manager):
    def login(self, email, password):
        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            print("Error handling!")
            return False
        if bcrypt.hashpw(password.encode("utf-8"), user.password.encode("utf-8")) == user.password.encode("utf-8"):
            return True
        else:
            return False
    def register(self,first_name, last_name, email, password, confirm_password):
        # we want to verify all the info and make sure that person is not already registered. <-- all of which cause errors!
        errors = {}
        if len(first_name) < 2:
            errors['first_name'] = "First Name is too short"
        if len(last_name) < 2:
            errors['last_name'] = "Last Name is too short"
        if len(password) < 8:
            errors['password'] = "Password is too short"
        if password != confirm_password:
            errors['confirm_password'] = "Passwords must match"
        user = self.get(email__iexact=email)
        if user:
            errors['invalid'] = "Invalid registration"
        if not EMAIL_REGEX.match(email):
            errors['email'] = "Please enter a valid email"
        if errors:
            return (False, errors)
        # register this person!
        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.create(first_name=first_name, last_name=last_name, password=password, email=email)
        return (True, self.get(email=email)[0])
        
# Create your models here.
class User(models.Model):
    # prebuilt with a manager called objects
    # managers allow us to do sql queries (either using object.raw <-- normal sql query)
    # ORM .get, .filter, find
    # we can now make a table (just like an erd diagram)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField() # auto validation for us!
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # super set of objects (its got everything objects has + login and register)
    userManager = UserManager()
    objects = models.Manager()

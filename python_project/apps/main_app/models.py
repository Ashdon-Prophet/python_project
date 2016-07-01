from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib import messages
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]*$')

class UserManager(models.Manager):
    def register(self, first_name, last_name, username, email, password, confirm_password):
        errors = {}
        if len(first_name) < 2:
            errors['first_name'] = "First Name is too short."
        if len(last_name) < 2:
            errors['last_name'] = "Last Name is too short."
        if len(password) < 8:
            errors['password'] = "Password is too short."
        if len(username) < 2:
            errors['username'] = "Username is too short."
        if password != confirm_password:
            errors['confirm_password'] = "Passwords do not match."
        if len(email) < 1:
            errors['email_blank'] = "Email cannot be blank."
        if not EMAIL_REGEX.match(email):
            errors['email'] = "Not a valid email address."
        user = self.filter(email__iexact=email)
        if user:
            errors['repeated'] = "Email already exists."
        if errors:
            return errors
        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.create(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        return False

    def login(self, email, password):
        user = self.get(email__iexact=email)
        if user and bcrypt.hashpw(password.encode('utf-8'), user.password.encode('utf-8')) == user.password:
            return (True, user)
        return (False, errors)

@python_2_unicode_compatible
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45, default="USERNAME")
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    description = models.TextField(max_length=500, default="DESCRIPTION")
    number_created = models.IntegerField(default=0)
    traded = models.IntegerField(default=0)
    owned = models.IntegerField(default=0)
    last_log = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()

    def __str__(self):
        return self.email


@python_2_unicode_compatible
class Creature(models.Model):
    HEAD_CHOICES = (
        ('Normal', 'Normal'),
        ('Wacky', 'Wacky'),
    )
    BODY_CHOICES = (
        ('Black Shirt', 'Black Shirt'),
        ('Blue Shirt', 'Blue Shirt'),
        ('Green Shirt', 'Green Shirt'),
        ('Grey Shirt', 'Grey Shirt'),
        ('Red Shirt', 'Red Shirt'),
    )
    ARM_CHOICES = (
        ('Ninja Shirt', 'Ninja Shirt'),
        ('Black T-Shirt', 'Black T-Shirt'),
        ('Blue T-Shirt', 'Blue T-Shirt'),
        ('Red T-Shirt', 'Red T-Shirt'),
        ('Green T-Shirt', 'Green T-Shirt'),
        ('Sleeveless T-Shirt', 'Sleeveless T-Shirt'),
    )
    LEG_CHOICES = (
        ('Blue Pants', 'Blue Pants'),
        ('Denim Plants', 'Denim Plants'),
        ('Black Shorts', 'Black Shorts'),
        ('Brown Shorts', 'Brown Shorts'),
        ('Denim Shorts', 'Denim Shorts'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    head_style = models.CharField(max_length=500, choices=HEAD_CHOICES, default='Normal')
    body_style = models.CharField(max_length=500, choices=BODY_CHOICES, default='Black Shirt')
    arm_style = models.CharField(max_length=500, choices=ARM_CHOICES, default='Black T-Shirt')
    leg_style = models.CharField(max_length=500, choices=LEG_CHOICES, default='Blue Pants')
    owner = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Trade(models.Model):
    user_sender = models.ForeignKey(User, related_name="sender")
    user_recipient = models.ForeignKey(User, related_name="recipient")
    creature_sent = models.ForeignKey(Creature, related_name="sent")
    creature_received = models.ForeignKey(Creature, related_name="received")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

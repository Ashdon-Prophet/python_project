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
    last_log = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()

    def __str__(self):
        return self.email

class Creature(models.Model):
    HEAD_CHOICES = (
        ('main_app/img/standard.png', 'Normal'),
        ('main_app/img/wacky.png', 'Wacky'),
    )
    BODY_CHOICES = (
        ('main_app/img/paleblackbody.png', 'Black Shirt'),
        ('main_app/img/palebluebody.png', 'Blue Shirt'),
        ('main_app/img/palegreenbody.png', 'Green Shirt'),
        ('main_app/img/palegreybody.png', 'Grey Shirt'),
        ('main_app/img/paleredbody.png', 'Red Shirt'),
    )
    ARM_CHOICES = (
        ('main_app/img/ninja.png', 'Ninja Shirt'),
        ('main_app/img/paleblackt.png', 'Black T-Shirt'),
        ('main_app/img/palebluet.png', 'Blue T-Shirt'),
        ('main_app/img/paleredt.png', 'Red T-Shirt'),
        ('main_app/img/palegreent.png', 'Green T-Shirt'),
        ('main_app/img/palesleveless.png', 'Sleeveless T-Shirt'),
    )
    LEG_CHOICES = (
        ('main_app/img/bluepants.png', 'Blue Pants'),
        ('main_app/img/denimpants.png', 'Denim Plants'),
        ('main_app/img/paleblackshorts.png', 'Black Shorts'),
        ('main_app/img/palebrownshorts.png', 'Brown Shorts'),
        ('main_app/img/bluepants.png', 'Denim Shorts'),
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

class Trade(models.Model):
    user_sender = models.ForeignKey(User, related_name="sender")
    user_recipient = models.ForeignKey(User, related_name="recipient")
    creature_sent = models.ForeignKey(Creature, related_name="sent")
    creature_received = models.ForeignKey(Creature, related_name="received")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

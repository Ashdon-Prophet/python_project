from __future__ import unicode_literals
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

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45, default="USERNAME")
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    created = models.IntegerField()    
    traded = models.IntegerField()
    last_log = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()


class Head(models.Model):
    style_name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Body(models.Model):
    style_name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Arm(models.Model):
    style_name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Leg(models.Model):
    style_name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Creature(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    head_style = models.ForeignKey(Head)
    body_style = models.ForeignKey(Body)
    arm_style = models.ForeignKey(Arm)
    leg_style = models.ForeignKey(Leg)
    owner = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

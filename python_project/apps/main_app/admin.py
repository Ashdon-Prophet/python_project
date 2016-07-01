from django.contrib import admin

# Register your models here.
from .models import User, Creature

admin.site.register(User)
admin.site.register(Creature)

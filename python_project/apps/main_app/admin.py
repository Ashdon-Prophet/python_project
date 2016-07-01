from django.contrib import admin

from .models import User, Creature
# Register your models here.

from .models import User, Creature

admin.site.register(User)
admin.site.register(Creature)

from django.contrib import admin
from .models import Species, Subspecies, Catch

# Register your models here.

admin.site.register(Species)
admin.site.register(Subspecies)
admin.site.register(Catch)
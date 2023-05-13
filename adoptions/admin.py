from django.contrib import admin

# Register your models here.
from .models import Pet, Vaccine

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']
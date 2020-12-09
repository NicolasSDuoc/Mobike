from django.contrib import admin
from .models import Commune, CustomUser,Credit_card,Bicycle, Parking
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm


admin.site.register(CustomUser)
admin.site.register(Commune)
admin.site.register(Credit_card)
admin.site.register(Bicycle)
admin.site.register(Parking)
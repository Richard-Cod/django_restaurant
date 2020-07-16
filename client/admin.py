from django.contrib import admin

# Register your models here.
from .models import Category,Food,Reason,Event,Info,Reservation

admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Reason)
admin.site.register(Event)
admin.site.register(Info)
admin.site.register(Reservation)
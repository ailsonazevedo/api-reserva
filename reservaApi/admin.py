from django.contrib import admin
from .models import Reservation, Key

# Register your models here.
@admin.register(Key)
class ChavesAdmin(admin.ModelAdmin):
    list_display = ['numero','nome']
    list_filter = ['nome','numero']


@admin.register(Reservation)
class ReservasAdmin(admin.ModelAdmin):
    list_display = ['key','first_name','date_reservation','date_devolution','reservation']
    list_filter = ['date_reservation','key','reservation']
    search_fields = ['key']



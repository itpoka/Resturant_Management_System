from django.contrib import admin
from .models import *



# Register your models here.
class deliveryAdmin(admin.ModelAdmin):
    list_display=['code','name','status','created_by','created_at']
    class Meta:
        model=Delivery

admin.site.register(Delivery,deliveryAdmin)

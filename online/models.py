from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.
class Delivery(models.Model):
    code = models.CharField(max_length=20,blank=True,null=True) 
    name = models.CharField(max_length=100,blank=True,null=True)
    status = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = UserForeignKey(auto_user_add=True,editable=False,related_name='delivery_creator')
    updated_by = UserForeignKey(auto_user=True,editable=False,related_name='delivery_updator')

    class Meta:
        db_table='ac_delivery'

    def _str_(self):
        return self.name
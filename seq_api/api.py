from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from seq_api.models import Gene

class UserResource(ModelResource):
  class Meta:
    queryset = User.objects.all()
    resource_name = 'user'
    excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
    allowed_methods = ['get']

class GeneResource(ModelResource):
  user = fields.ForeignKey(UserResource, 'user')
  class Meta:
    queryset = Gene.objects.all()
    resource_name = 'gene'








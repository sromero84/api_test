from tastypie.resources import ModelResource
from tastypie import fields
from scratchers.models import Scratcher, Size
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication


class ScratcherResource(ModelResource):
    item_sizes = fields.ToManyField(
        'scratchers.api.SizeResource', 'item_sizes', null=True, full=True)

    class Meta:
        queryset = Scratcher.objects.all()
        resource_name = 'scratcher'
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put']


class SizeResource(ModelResource):
    class Meta:
        queryset = Size.objects.all()
        resource_name = 'size'
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put']

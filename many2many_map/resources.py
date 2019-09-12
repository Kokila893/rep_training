from falcon_autocrud.resource import CollectionResource, SingleResource
from vehicle.models import User, Car
import falcon

# class CarCollectionResource(CollectionResource):
#     model = Car
#     methods = ['GET', 'POST']
#     allow_subresources = True
#
#     # def on_post(self, req, resp, *args, **kwargs):
#     #     pass
#
# class CarSingleResource(SingleResource):
#     model = Car
#
#
#
# class UserCollectionResource(CollectionResource):
#     model = User
#     methods = ['GET', 'POST']
#     allow_subresources = True
#
#     # def on_post(self, req, resp, *args, **kwargs):
#     #     pass


class UserCollectionResource(CollectionResource):
    model = User
    methods = ['GET', 'POST']
    allow_subresources = True


class UserResource(SingleResource):
    model = User


class CarCollectionResource(CollectionResource):
    model = Car

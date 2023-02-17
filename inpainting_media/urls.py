

from django.urls import include, path
from rest_framework import routers
from inpainting_media.apis.v1 import inpaintingAPI
# router = routers.SimpleRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# router.register('medias', views.MediaViewSet, basename='media')
# router.register('/media-list', animeMediaAPI.get_medias)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('medias',inpaintingAPI.get_medias,name='get_medias'),
    path('upload-media',inpaintingAPI.upload_media,name='upload_media'),

]

from app.settings import STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.files.storage import default_storage
from django.contrib.sites.shortcuts import get_current_site
import os
import uuid
import logging
from inpainting_media.models import MediaModel
from django.core.files.storage import FileSystemStorage


logger = logging.getLogger(__name__)


@api_view(['GET'])
def get_medias(request):
    try:
        return Response({
            "status_code": status.HTTP_200_OK,
            "message": f"Get media list successfully",
        })

    except Exception as e:
        message = f"error: {e}"
        return Response({
            "status_code": status.HTTP_404_NOT_FOUND,
            "message": f"error : {e}"
        }, status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_media(request):
    pass


@api_view(['POST'])
def upload_media(request):
    try:

        prompts = request.POST.get('prompts')
        file_obj = request.FILES['file']
        model = request.POST.get('model')
        media = MediaModel()
        media.title = prompts
        
        # defaults to   MEDIA_ROOT
        prompts = str(prompts).replace(' ','-')
        sub_location  = f'{prompts}'
        file_location = f'media/{sub_location}'
        fs = FileSystemStorage(location=file_location)
        filename = fs.save(file_obj.name, file_obj)
        filename = f'{sub_location}/{filename}' 
        file_url = fs.url(filename)

        media.media_file = filename

        media.save()

        return Response({
            "status_code": status.HTTP_200_OK,
            "message": f"Upload successfully",
            "data": file_url
        })

    except Exception as e:
        message = f"error: {e}"
        return Response({
            "status_code": status.HTTP_404_NOT_FOUND,
            "message": f"error : {e}"
        }, status.HTTP_404_NOT_FOUND)

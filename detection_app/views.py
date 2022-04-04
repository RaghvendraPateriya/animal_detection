import base64
import io
from io import BytesIO
from datetime import datetime

from PIL import Image
from django.core.files import File
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from . import models
from .serializers import ClientSerializer, ClientUploadedImageSerializer


class AnimalImage(viewsets.ViewSet):

    def create(self, request):
        """ Create AnimalImage Object."""
        image = request.data.get('image')
        label = request.data.get('label')
        client_secret_key = request.data.get('client_secret_key')
        try:
            client = models.Client.objects.get(secret_key=client_secret_key)
        except models.Client.DoesNotExist as exc:
            return Response({'msg': str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'msg': 'Missing/Incorrect payload.'},
                            status=status.HTTP_400_BAD_REQUEST)
        if not all([image, client_secret_key, client]):
            return Response({'msg': 'Missing/Incorrect payload.'},
                            status=status.HTTP_400_BAD_REQUEST)
        # Parse Image Back to Original format
        img_bytes = base64.b64decode(image.encode('utf-8'))
        img = Image.open(io.BytesIO(img_bytes))
        image_io = BytesIO()
        img.save(image_io, 'JPEG')
        current_date_time = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
        thumbnail = File(image_io,
                         name=f'{client.name}-{label}-{current_date_time}.jpeg')
        obj = models.AnimalImage(label=label, image=thumbnail, uploaded_by=client)
        obj.save()
        # TODO: The server will detect the animal and send it back to the client.
        return Response({'msg': 'Image uploaded successfully'},
                        status=status.HTTP_201_CREATED)


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = models.Client.objects.all()

    @action(detail=True, methods=['GET'], name='Get Uploaded Image')
    def images(self, request, pk=None):
        """ Get User/Client Uploaded images"""
        queryset = models.Client.objects.get(pk=pk)
        serializer = ClientUploadedImageSerializer(queryset)
        return Response(serializer.data)

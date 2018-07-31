from django.shortcuts import render
from .models import description
from .serializers import descriptionSerializer
from rest_framework import viewsets
#from rest_framework.decorators import action
#from rest_framework.response import Response

class descriptionview(viewsets.ModelViewSet):
	queryset=description.objects.all()
	serializer_class=descriptionSerializer
	#@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])



from rest_framework import viewsets, status
from rest_framework.response import Response

from projeler_api import serializers
from projeler_api import models
# Create your views here.


class PersonelListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PersonelSerializer
    queryset = models.Personel.objects.all()



class ProjeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectListSerializer
    detail_serializer_class = serializers.ProjectDetailSerializer
    queryset = models.Project.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self,'detail_serializer_class'):
                return self.detail_serializer_class
            
        return super(ProjeViewSet, self).get_serializer_class()



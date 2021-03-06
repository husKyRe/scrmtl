"""Controller methods in the app for cards
"""
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions, status, mixins, generics
from api.views.nested_ressources_helper import NestedComponentViewSet, \
    NestedMtmMixin

from django.shortcuts import get_object_or_404

from rules.contrib.rest_framework import AutoPermissionViewSetMixin

from .. import models
from .. import serializers


class BoardViewSet(AutoPermissionViewSetMixin,
                   NestedMtmMixin,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   NestedComponentViewSet):
    """CRUD for Boards
    """
    queryset = models.Board.objects.all()

    def get_queryset(self):
        if 'project_pk' not in self.kwargs:
            return super().get_queryset()
        else:
            return super().get_queryset().filter(project=self.kwargs['project_pk'])
    serializer_class = serializers.BoardSerializer

    def retrieve(self, request, *args, pk=None, **kwargs):
        """retrive for full and partial retrieve
            Add ?DetailLevel=full for full data
            """
        detaillevel = self.request.query_params.get('DetailLevel', None)
        if detaillevel is not None:
            if detaillevel == 'full':
                instance = self.get_object()
                serializer = serializers.BoardSerializerFull(instance)
                return Response(serializer.data)

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

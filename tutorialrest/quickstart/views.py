from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from tutorialrest.quickstart.serializers import GroupSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """ endpioint que permite a los usuarios ver o editar """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """ endpoint que permite a los grupos ver o editar """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
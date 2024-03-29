from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer
from api import serializers
from api import models
from collections import OrderedDict


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]


class RealEstateOwnerViewSet(viewsets.ModelViewSet):

    queryset = models.RealEstateOwner.objects.all()
    serializer_class = serializers.RealEstateOwnerSerializer
    permission_classes = [permissions.AllowAny]


class RealEstatesViewSet(viewsets.ModelViewSet):

    queryset = models.RealEstate.objects.all()
    serializer_class = serializers.RealEstatesSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = [
        'owner',
        'area_type',
        'region',
        'realestate_type',
        'period',
        'relation',
        'dt',
    ]


class FreelanceAgentViewSet(viewsets.ModelViewSet):

    queryset = models.FreelanceAgent.objects.all()
    serializer_class = serializers.AgencySerializer
    permission_classes = [permissions.AllowAny]


class AgentInvestorViewSet(viewsets.ModelViewSet):

    queryset = models.AgentInvestor.objects.all()
    serializer_class = serializers.AgentInvestorSerializer
    permission_classes = [permissions.AllowAny]


class AgencyViewSet(viewsets.ModelViewSet):

    queryset = models.Agency.objects.all()
    serializer_class = serializers.AgentInvestorSerializer
    permission_classes = [permissions.AllowAny]


class AgencyWorkerViewSet(viewsets.ModelViewSet):

    queryset = models.AgencyWorker.objects.all()
    serializer_class = serializers.AgencyWorkerSerializer
    permission_classes = [permissions.AllowAny]


class TagViewSet(viewsets.ModelViewSet):

    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = [permissions.AllowAny]


class PriceStoryViewSet(viewsets.ModelViewSet):

    queryset = models.PriceStory.objects.all()
    serializer_class = serializers.PriceStorySerializer
    permission_classes = [permissions.AllowAny]


class GoldViewSet(viewsets.ModelViewSet):

    queryset = models.Gold.objects.order_by('-dt')[:1]
    serializer_class = serializers.GoldSerializer
    permission_classes = [permissions.AllowAny]

class DollarViewSet(viewsets.ModelViewSet):

    queryset = models.Dollar.objects.order_by('-dt')[:1]
    serializer_class = serializers.DollarSerializer
    permission_classes = [permissions.AllowAny]


class EuroViewSet(viewsets.ModelViewSet):

    queryset = models.Euro.objects.order_by('-dt')[:1]
    serializer_class = serializers.EuroSerializer
    permission_classes = [permissions.AllowAny]


class BtcViewSet(viewsets.ModelViewSet):

    queryset = models.Btc.objects.order_by('-dt')[:1]
    serializer_class = serializers.BtcSerializer
    permission_classes = [permissions.AllowAny]


class CustomViewSet(viewsets.ModelViewSet):

    queryset = models.RealEstate.objects.all()
    serializer_class = serializers.CustomSerializer
    permission_classes = [permissions.AllowAny]


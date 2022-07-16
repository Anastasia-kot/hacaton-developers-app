from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer
from api import serializers
from api import model


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class RealEstateOwnerViewSet(viewsets.ModelViewSet):

    queryset = models.RealEstateOwner.objects.all()
    serializer_class = serializers.RealEstateOwnerSerializer
    permission_classes = [permissions.IsAuthenticated]


class RealEstatesViewSet(viewsets.ModelViewSet):

    queryset = models.RealEstate.objects.all()
    serializer_class = serializers.RealEstatesSerializer
    permission_classes = [permissions.IsAuthenticated]


class FreelanceAgentViewSet(viewsets.ModelViewSet):

    queryset = models.Agent.objects.all()
    serializer_class = serializers.AgencySerializer
    permission_classes = [permissions.IsAuthenticated]


class AgentInvestorViewSet(viewsets.ModelViewSet):

    queryset = models.AgentInvestor.objects.all()
    serializer_class = serializers.AgentInvestorSerializer
    permission_classes = [permissions.IsAuthenticated]


class AgencyViewSet(viewsets.ModelViewSet):

    queryset = models.Agency.objects.all()
    serializer_class = serializers.AgentInvestorSerializer
    permission_classes = [permissions.IsAuthenticated]


class AgencyWorkerViewSet(viewsets.ModelViewSet):

    queryset = models.AgencyWorker.objects.all()
    serializer_class = serializers.AgencyWorkerSerializer
    permission_classes = [permissions.IsAuthenticated]


class TagViewSet(viewsets.ModelViewSet):

    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class PriceStoryViewSet(viewsets.ModelViewSet):

    queryset = models.PriceStory.objects.all()
    serializer_class = serializers.PriceStorySerializer
    permission_classes = [permissions.IsAuthenticated]


class GoldViewSet(viewsets.ModelViewSet):

    queryset = models.Gold.objects.all()
    serializer_class = serializers.GoldSerializer
    permission_classes = [permissions.IsAuthenticated]

class DollarViewSet(viewsets.ModelViewSet):

    queryset = models.Dollar.objects.all()
    serializer_class = serializers.DollarSerializer
    permission_classes = [permissions.IsAuthenticated]


class EuroViewSet(viewsets.ModelViewSet):

    queryset = models.Euro.objects.all()
    serializer_class = serializers.EuroSerializer
    permission_classes = [permissions.IsAuthenticated]


class BtcViewSet(viewsets.ModelViewSet):

    queryset = models.Btc.objects.all()
    serializer_class = serializers.BtcSerializer
    permission_classes = [permissions.IsAuthenticated]

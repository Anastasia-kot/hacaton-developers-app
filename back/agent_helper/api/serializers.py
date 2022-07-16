from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api import models


class UserSerializer(serializers.HyperlinkedModelSerializer):

    """ User model serializer """

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    """ Group model serializer """

    class Meta:
        model = Group
        fields = ['url', 'name']

class RealEstateOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RealEstateOwner
        fields = '__all__'


class RealEstatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RealEstate
        fields = '__all__'


class FreelanceAgentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.FreelanceAgent
        fields = '__all__'


class AgentInvestorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AgentInvestor
        fields = '__all__'


class AgencySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Agency
        fields = '__all__'


class AgencyWorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AgencyWorker
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = '__all__'


class PriceStorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PriceStory
        fields = '__all__'



class GoldSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Gold
        fields = '__all__'

class DollarSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Dollar
        fields = '__all__'


class EuroSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Euro
        fields = '__all__'


class BtcSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Btc
        fields = '__all__'


class CustomSerializer(serializers.ModelSerializer):
    
    gold = GoldSerializer(many=True)
    euro = EuroSerializer(many=True)
    dollar = DollarSerializer(many=True)
    btc = BtcSerializer(many=True)

    class Meta:
        model = models.RealEstate
        fields = [
            'owner',
            'area_type',
            'region',
            'realestate_type',
            'period',
            'relation',
            'dt',
        ]

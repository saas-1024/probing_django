import io

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import CryptoAsset
from .models import SpotDeal
from .models import ClosedSpotDeal


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class SpotDealSerializer(serializers.ModelSerializer):
    # date_deal = serializers.DateTimeField(auto_now=True)
    asset_amount = serializers.DecimalField(max_digits=32, decimal_places=8)
    usd_amount = serializers.DecimalField(max_digits=16, decimal_places=8)
    comission = serializers.DecimalField(max_digits=16, decimal_places=8)
    exchange = serializers.CharField(max_length=64)
    trade_pair = serializers.CharField(max_length=32, default='USDT')
    trade_side = serializers.CharField(max_length=1, default='B')  # B - buy, S - sell
    comment = serializers.CharField(max_length=128)
    # user_deal = CustomUserSerializer(read_only=True)
    user_deal = UserSerializer()
    asset_deal = serializers.IntegerField()

    class Meta:
        model = SpotDeal
        fields = ('asset_amount', 'usd_amount', 'comment', 'exchange', 'comission', 'trade_pair', 'trade_side',
                  "user_deal", 'asset_deal')

    def create(self, validated_data):
        return SpotDeal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.asset_amount = validated_data.get("asset_amount")
        instance.usd_amount = validated_data.get("usd_amount")
        instance.comission = validated_data.get("comission")
        instance.exchange = validated_data.get("exchange")
        instance.trade_pair = validated_data.get("trade_pair")
        instance.trade_side = validated_data.get("trade_side")
        instance.comment = validated_data.get("comment")
        instance.save()
        return instance

    def delete(self, instance, validated_data):
        instance.asset_amount = validated_data.get("asset_amount")
        instance.usd_amount = validated_data.get("usd_amount")
        instance.comission = validated_data.get("comission")
        instance.exchange = validated_data.get("exchange")
        instance.trade_pair = validated_data.get("trade_pair")
        instance.trade_side = validated_data.get("trade_side")
        instance.comment = validated_data.get("comment")
        instance.delete()
        return str("Deal deleted")


class CryptoAssetSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    ticker = serializers.CharField()
    consensus_type = serializers.CharField()
    token_birth_date = serializers.DateField()

    class Meta:
        model = CryptoAsset
        fields = ('full_name', 'ticker', 'consensus_type', 'token_birth_date')

    def create(self, validated_data):
        return CryptoAsset.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get("full_name")
        instance.ticker = validated_data.get("ticker")
        instance.consensus_type = validated_data.get("consensus_type")
        instance.token_birth_date = validated_data.get("token_birth_date")
        instance.save()
        return instance

    def delete(self, instance, validated_data):
        instance.full_name = validated_data.get("full_name")
        instance.ticker = validated_data.get("ticker")
        instance.consensus_type = validated_data.get("consensus_type")
        instance.token_birth_date = validated_data.get("token_birth_date")
        instance.delete()
        return str("Row deleted")


class ClosedSpotDealSerializer(serializers.Serializer):
    # date_deal_closed = serializers.DateTimeField(auto_now=True)
    asset_amount = serializers.DecimalField(max_digits=32, decimal_places=8)
    usd_earned = serializers.DecimalField(max_digits=16, decimal_places=8)
    comission = serializers.DecimalField(max_digits=16, decimal_places=8)
    exchange = serializers.CharField(max_length=64)
    trade_pair = serializers.CharField(max_length=32, default='USDT')
    comment = serializers.CharField(max_length=128)

    # user_deal_closed = CustomUserSerializer(read_only=True)
    # asset_deal_closed = serializers.IntegerField()
    # from_buy_deal = serializers.IntegerField()

    class Meta:
        model = ClosedSpotDeal
        fields = ('asset_amount', 'usd_earned', 'comment', 'exchange', 'comission', 'trade_pair', )

    def create(self, validated_data):
        return ClosedSpotDeal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.asset_amount = validated_data.get("asset_amount")
        instance.usd_earned = validated_data.get("usd_earned")
        instance.comission = validated_data.get("comission")
        instance.exchange = validated_data.get("exchange")
        instance.trade_pair = validated_data.get("trade_pair")
        instance.comment = validated_data.get("comment")
        instance.save()
        return instance

    def delete(self, instance, validated_data):
        instance.asset_amount = validated_data.get("asset_amount")
        instance.usd_earned = validated_data.get("usd_earned")
        instance.comission = validated_data.get("comission")
        instance.exchange = validated_data.get("exchange")
        instance.trade_pair = validated_data.get("trade_pair")
        instance.comment = validated_data.get("comment")
        instance.delete()
        return str("Closed deal deleted")


# class CryptoAssetModel:
#     def __init__(self, title, content):
#         self.full_name = title
#         self.ticker = content


# def encode():
#     model = CryptoAssetModel('pidr', 'pidr')
#     model_sr = CryptoAssetSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"pidr","content":"pidr"}')
#     data = JSONParser().parse(stream)
#     serializer = CryptoAssetSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)

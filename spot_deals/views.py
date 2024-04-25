from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import AnonymousUser, User

from .models import CryptoAsset
from .models import SpotDeal
from .models import ClosedSpotDeal
from .serializers import SpotDealSerializer
from .serializers import CryptoAssetSerializer
from .serializers import ClosedSpotDealSerializer



def index(request):
    return HttpResponse("Страница спотовых сделок")


def assets(request, asset_id):
    return HttpResponse(f"<h1>Page with assets</h1><p>{asset_id}</p>")


def archive(request, year):
    if int(year) > 2024:
        return redirect('home_page')

    return HttpResponse(f"<h1>Assets archive by years</h1><p>{year}</p>")


class SpotDealsAPIView(APIView):
    # queryset = SpotDeal.objects.all()
    # serializer_class = SpotDealSerializer

    def get(self, request):
        spisok_deals = SpotDeal.objects.all()
        return Response({'Сделки': SpotDealSerializer(spisok_deals, many=True).data})

    def post(self, request):
        user_id = request.data.get('user_deal')
        asset_id = request.data.get('asset_deal')

        user_instance = User.objects.get(pk=user_id)
        asset_instance = CryptoAsset.objects.get(pk=asset_id)
        serializer = SpotDealSerializer(data={
            'asset_amount': request.data.get('asset_amount'),
            'usd_amount': request.data.get('usd_amount'),
            'comission': request.data.get('comission'),
            'exchange': request.data.get('exchange'),
            'trade_pair': request.data.get('trade_pair'),
            'trade_side': request.data.get('trade_side'),
            'comment': request.data.get('comment'),
            'user_deal': user_instance,
            'asset_deal': asset_instance,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data}, status=status.HTTP_201_CREATED)

        # user = request.user
        # user_queryset = User.objects.filter(id=user.id)
        # print('@@@@@@@@ ', user_queryset)
        # if isinstance(user, AnonymousUser):
        #     return Response(status=400, data={'message': 'User not authtorized'})
        # request_data = request.data.copy()
        # request_data['user_deal'] = user
        # serializer = SpotDealSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response({'post': serializer.data})

    def put(self, requset, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = SpotDeal.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"})
        serializer = SpotDealSerializer(data=requset.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        instance = SpotDeal.objects.get(pk=pk)
        instance.delete()
        return Response({"post": "Delete spot deal row " + str(pk)})


class CryptoAssetsAPIView(APIView):

    def get(self, request):
        spisok = CryptoAsset.objects.all()
        return Response({'Активы ': CryptoAssetSerializer(spisok, many=True).data})

    def post(self, request):
        serializer = CryptoAssetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = CryptoAsset.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"})
        serializer = CryptoAssetSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        instance = CryptoAsset.objects.get(pk=pk)
        instance.delete()
        return Response({"post": "Delete asset row " + str(pk)})


class ClosedSpotDealAPIView(APIView):
    def get(self, request):
        spisok_deals_closed = ClosedSpotDeal.objects.all()
        return Response({'Закрытые сделки': ClosedSpotDealSerializer(spisok_deals_closed, many=True).data})

    def post(self, request):
        serializer = ClosedSpotDealSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, requset, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = ClosedSpotDeal.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"})
        serializer = ClosedSpotDealSerializer(data=requset.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        instance = ClosedSpotDeal.objects.get(pk=pk)
        instance.delete()
        return Response({"post": "Delete closed spot deal row " + str(pk)})


# Example code of getting and saving data through the model
# class UserList(View):
#
#     def get(self, request):
#         users = User.objects.all()
#         # data = list(users.values())
#         data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]  # List compr
#         return JsonResponse(data, safe=False)
#
#     def post(self, request):
#         data = json.loads(request.body)
#         # username = data.get("username")
#         email = data.get("email")
#         first_name = data.get("first_name")
#         last_name = data.get("last_name")
#         user = User.objects.create_user(email, first_name, last_name)
#         return JsonResponse({"status": "OK"}, status=HTTPStatus.CREATED)
#
#

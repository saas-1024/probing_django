from django.contrib import admin
from django.urls import path, include

from spot_deals.views import index, SpotDealsAPIView, CryptoAssetsAPIView, ClosedSpotDealAPIView
from spot_deals.views import assets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('spot_deals.urls')),
    # path('api/spot_deals/', SpotDealsAPIView.as_view()),
    path('api/crypto_assets/', CryptoAssetsAPIView.as_view()),
    path('api/crypto_assets/<int:pk>', CryptoAssetsAPIView.as_view()),
    path('api/spot_deals/', SpotDealsAPIView.as_view()),
    path('api/spot_deals/<int:pk>', SpotDealsAPIView.as_view()),
    path('api/closed_spot_deals/', ClosedSpotDealAPIView.as_view()),
    path('api/closed_spot_deals/<int:pk>', ClosedSpotDealAPIView.as_view()),
]

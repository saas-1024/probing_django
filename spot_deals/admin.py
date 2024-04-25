from django.contrib import admin

from .models import CryptoAsset
from .models import SpotDeal
from .models import ClosedSpotDeal

admin.site.register(CryptoAsset)
admin.site.register(SpotDeal)
admin.site.register(ClosedSpotDeal)


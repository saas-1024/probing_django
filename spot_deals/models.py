from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class CryptoAsset(models.Model):
    full_name = models.CharField('Crypto asset', max_length=64)
    ticker = models.CharField('Ticker', max_length=16)
    consensus_type = models.CharField('Consensus', max_length=32)
    token_birth_date = models.DateField('Date of project issue')

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return f'{self.full_name} ({self.pk})'


class SpotDeal(models.Model):
    date_deal = models.DateTimeField('Date deal', auto_now=True)
    asset_amount = models.DecimalField(default=0, max_digits=32, decimal_places=8)
    usd_amount = models.DecimalField(default=0, max_digits=16, decimal_places=8)
    comission = models.DecimalField(default=0, max_digits=16, decimal_places=8)
    exchange = models.CharField('Криптобиржа', max_length=64)
    trade_pair = models.CharField('Торговая пара', max_length=32, default='USDT')
    trade_side = models.CharField('Deal side', max_length=1, default='B')  # B - buy, S - sell
    comment = models.CharField('Deal comment', max_length=128)
    user_deal = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name='user_deals'
    )
    asset_deal = models.ForeignKey(
        CryptoAsset, on_delete=models.RESTRICT, related_name='asset_deals'
    )

    class Meta:
        ordering = ['-date_deal']

    def __str__(self):
        return f'{self.trade_pair} ({self.pk})'


class ClosedSpotDeal(models.Model):
    date_deal_closed = models.DateTimeField('Date sell', auto_now=True)
    asset_amount = models.DecimalField(default=0, max_digits=32, decimal_places=8)
    usd_earned = models.DecimalField(default=0, max_digits=16, decimal_places=8)
    comission = models.DecimalField(default=0, max_digits=16, decimal_places=8)
    exchange = models.CharField('Криптобиржа', max_length=64)
    trade_pair = models.CharField('Торговая пара', max_length=32, default='USDT')
    comment = models.CharField('Deal comment', max_length=128)
    user_deal_closed = models.ForeignKey(
        User, models.RESTRICT, 'user_deal_closed'
    )
    asset_deal_closed = models.ForeignKey(
        CryptoAsset, models.RESTRICT, 'asset_deals_closed'
    )
    from_buy_deal = models.ForeignKey(
        SpotDeal, models.RESTRICT, 'from_buy_deal'
    )

    class Meta:
        ordering = ['-date_deal_closed']

    def __str__(self):
        return f'{self.trade_pair} ({self.pk})'

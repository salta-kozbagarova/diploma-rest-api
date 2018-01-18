from django.db import models
from auction.common.models import Product
from auction.common.models import AuctionBaseModel

# Create your models here.
class ProductImage(AuctionBaseModel):
    #product_id = models.ForeignKey(Product, on_delete=models.CASCADE, default=0)
    image = models.CharField(max_length=255)
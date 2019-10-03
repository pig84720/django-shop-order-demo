from django.db import models

# 目前推測要有vip身份才能購買vip商品


class Product(models.Model):
    product_id = models.AutoField(primary_key=True, verbose_name=u'商品id')
    stock_pcs = models.PositiveIntegerField(verbose_name=u'商品庫存數量')
    price = models.PositiveIntegerField(verbose_name=u'商品單價')
    shop_id = models.CharField(max_length=5, verbose_name=u'商品所屬館別')
    vip = models.BooleanField(
        default=True, verbose_name=u'是否為VIP', help_text=u'True => VIP限定/ False =>無限制購買對象')

    class Meta:
        verbose_name = u'商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return u'商品id(%d)館別(%s)' % (self.product_id, self.shop_id)


class OrdersManager(models.Manager):
    def get_queryset(self):
        # 隱藏刪除的項
        return super().get_queryset().filter(is_delete=False)


class Order(models.Model):
    id = models.AutoField(primary_key=True, verbose_name=u'訂單id')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=u'商品')
    qty = models.PositiveIntegerField(verbose_name=u'購買數量')
    customer_id = models.PositiveIntegerField(verbose_name=u'Customer ID')
    is_delete = models.BooleanField(default=False, verbose_name=u'是否刪除')

    objects = OrdersManager()

    class Meta:
        verbose_name = u'訂單'
        verbose_name_plural = verbose_name

    def __str__(self):
        return u'訂單id(%s)' % self.id

    def price(self):
        return self.product.price
    price.short_description = u'商品單價'

    def shop_id(self):
        return self.product.shop_id
    shop_id.short_description = u'商品所屬館別'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

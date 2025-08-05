from rest_frameworks import serializers
from .models import Orders, OrderItems

class OrderItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['item_name', 'item_price', 'qnty']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
        read_only = ['order_id', 'total_order', 'created_at']

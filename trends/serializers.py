from rest_framework.serializers import ModelSerializer
from .models import Trend,TrendNews

class TrendSerializer(ModelSerializer):
    class Meta:
        model = Trend
        fields = "__all__"

class TrendNewsSerializer(ModelSerializer):
    class Meta:
        model = TrendNews
        fields = "__all__"
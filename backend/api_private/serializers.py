from rest_framework import serializers
from .models import PlanInvestment


class PlanInvestmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlanInvestment
        fields = '__all__'
        # fields = ('id','question','answer','is_published')






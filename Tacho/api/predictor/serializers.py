from rest_framework import serializers
from predictor.models import Predictor

class PredictorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predictor
        fields = '__all__'
        
    def validate(self, data):
        
        if data['fecha_inicial'] > data['fecha_final']:
            raise serializers.ValidationError("Error, la fecha inicial no puede ser mayor a la fecha final.")
        return data
from rest_framework import serializers
from .models import (
    BasicTusi,
    BasicXiajing,
    BasicZhiguan,
    BasicZhudi,
    RelationshipTusi,
    RelationshipXiajing,
    RelationshipZhiguan,
    RelationshipZhudi
)

class BasicTusiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicTusi
        fields = '__all__'

class BasicXiajingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicXiajing
        fields = '__all__'

class BasicZhiguanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicZhiguan
        fields = '__all__'

class BasicZhudiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicZhudi
        fields = '__all__'

class RelationshipTusiSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationshipTusi
        fields = '__all__'

class RelationshipXiajingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationshipXiajing
        fields = '__all__'

class RelationshipZhiguanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationshipZhiguan
        fields = '__all__'

class RelationshipZhudiSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationshipZhudi
        fields = '__all__'
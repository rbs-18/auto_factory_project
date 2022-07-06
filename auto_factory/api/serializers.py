from django.forms import FloatField
from rest_framework import serializers

from .models import Cost, Detail, DetailParameter, Parameter


class ParameterSerializer(serializers.ModelSerializer):
    """ Serializer for parameters. """

    class Meta:
        model = Parameter
        exclude = ('id',)


class DetailSerializer(serializers.ModelSerializer):
    """ Serializer for details. """

    parameters = ParameterSerializer(many=True, required=False)

    class Meta:
        model = Detail
        fields = ('type_name', 'price', 'amount', 'parameters')

    def create(self, validated_data):
        if 'parameters' not in self.initial_data:
            detail = Detail.objects.create(**validated_data)
            return detail

        parameters = validated_data.pop('parameters')

        detail = Detail.objects.create(**validated_data)

        for parameter in parameters:
            current_parameter, status = Parameter.objects.get_or_create(
                **parameter,
            )
            DetailParameter.objects.create(
                parameter=current_parameter, detail=detail
            )
        return detail


class DetailListSerializer(serializers.ModelSerializer):
    """ Serializer for detail list. """

    class Meta:
        model = Detail
        fields = ('id', 'type_name', 'price', 'amount')


class CostSerializer(serializers.ModelSerializer):
    """ Serializer for cost. """

    class Meta:
        model = Cost
        fields = '__all__'
        read_only_fields = ('prime_cost', 'finall_price')

    def validate_margin(self, value):
        if int(value) <= 0:
            raise serializers.ValidationError(
                'Проверьте значение процента наценки!'
            )
        return value

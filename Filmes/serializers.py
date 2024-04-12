from rest_framework import serializers, status
from rest_framework.response import Response




class  AvaliacaoSerializer(serializers.Serializer):
    comentario = serializers.CharField()
    nota = serializers.IntegerField()
    filme = serializers.IntegerField()

    def validate(self, data):
        if data['nota'] < 0 or data['nota'] > 5:
            raise serializers.ValidationError("A nota deve ser um número entre 0 e 5.")
        return data
    

class  AvaliacaoUpdateSerializer(serializers.Serializer):
    comentario = serializers.CharField(required=False)
    nota = serializers.IntegerField(required=False)

    def validate(self, data):
        if 'nota' not in data:
            return data
        else:
            if data['nota'] < 0 or data['nota'] > 5:
                raise serializers.ValidationError("A nota deve ser um número entre 0 e 10.")
            return data
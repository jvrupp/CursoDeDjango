from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import requests
from .models import Usuario

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    cpf = serializers.CharField(write_only=True)
    telefone = serializers.CharField(write_only=True)
    endereco = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'confirm_password', 'cpf', 'telefone', 'endereco', 'first_name', 'last_name', 'email']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("As senhas não são iguais.")
        response = requests.get(f'https://viacep.com.br/ws/{data["endereco"]}/json/')
        print(response.json())
        if response.json().get('erro'):
            raise serializers.ValidationError("CEP inválido.")
        
        return data

    def create(self, validated_data):
        print(validated_data)   
        validated_data.pop('confirm_password')  # Remove confirm_password from validated data
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        return super(UserSerializer, self).create(validated_data)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HelloSerializer


class HelloView(APIView):
    """Test API View"""
    serializers_class = HelloSerializer

    def get(self, request):
        an_apiview = [
            'Hello',
            'Salom'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


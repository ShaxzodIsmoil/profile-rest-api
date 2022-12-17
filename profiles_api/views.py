from rest_framework.views import APIView
from rest_framework.response import Response


class HelloView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        an_apiview = [
            'Hello',
            'Salom'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

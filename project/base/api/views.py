"""Views for api"""
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    
@api_view(['GET'])
def get_routes(request):
    """gets the routes

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)



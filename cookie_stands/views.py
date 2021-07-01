from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Cookie
from .permissions import IsPurchasherOrReadOnly
from .serializers import CookieSerializer


class CookieList(ListCreateAPIView):
    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer


class CookieDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsPurchasherOrReadOnly,)
    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer

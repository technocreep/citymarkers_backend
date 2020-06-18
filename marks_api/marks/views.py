from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import Mark
from .serializers import MarkSerializer
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth import authenticate


# class AllMarks(generics.ListCreateAPIView):
class AllMarks(viewsets.ModelViewSet):
# class AllMarks(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    # permission_classes = [IsAuthenticated]
    # def get(self, request):

    #     queryset = Mark.objects.all()
    #     serializer_class = MarkSerializer(queryset, many=True)
    #     return Response({'allmarks':serializer_class.data})
    
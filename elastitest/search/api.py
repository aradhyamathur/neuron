from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from .models import PersonDb
from .serialyzers import PersonSerializer


class PersonList(ListAPIView):

    serializer_class = PersonSerializer
    queryset = PersonDb.objects.all()


class PersonCreate(ListCreateAPIView):

    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        data = self.request.data
        print data
        ser = PersonSerializer(data={'name': self.request.data['name'],
                                     'age': self.request.data['age'],
                                     'address': self.request.data['address']})
        if ser.is_valid():
            ser.save()


class PersonDetailView(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        qs = PersonDb.objects.filter(name=self.kwargs['name'])
        return qs

from rest_framework.generics import ListAPIView
from serialyzers import StudentSerializer
from .models import Student


class StudentList(ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()



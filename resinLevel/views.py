# views.py
from rest_framework import viewsets

from .serializers import PrintSerializer, PrinterSerializer, ResinSerializer
from .models import Print, Printer, Resin


class ResinViewSet(viewsets.ModelViewSet):
    queryset = Resin.objects.all()
    serializer_class = ResinSerializer


class PrinterViewSet(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer


class PrintViewSet(viewsets.ModelViewSet):
    queryset = Print.objects.all()
    serializer_class = PrintSerializer

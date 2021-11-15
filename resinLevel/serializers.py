from rest_framework import serializers

from .models import Printer, Print, Resin


class ResinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resin
        fields = ('name', 'price')


class PrinterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Printer
        fields = ('name', 'resinLeft', 'lastClean', 'resinMount')


class PrintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Print
        fields = ('name', 'weight', 'predictedTime', 'printerPredictedTime', 'state', 'printer', 'date')

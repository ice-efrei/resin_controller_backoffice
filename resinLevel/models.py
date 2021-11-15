from datetime import datetime

from django.db import models


PRINT_STATE = [
    (0, "standby"),
    (1, "success"),
    (2, "failure")
]


class Resin(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return "resin-" + str(self.id) + " : " + self.name


class Printer(models.Model):
    name = models.CharField(max_length=255)
    resinLeft = models.FloatField(null=True, blank=True)
    lastClean = models.DateField(null=True, blank=True)
    resinMount = models.ForeignKey(Resin, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "printer-" + str(self.id) + " : " + self.name


class Print(models.Model):
    name = models.CharField(max_length=255)
    weight = models.FloatField(null=True, blank=True)
    predictedTime = models.FloatField(null=True, blank=True)
    printerPredictedTime = models.FloatField(null=True, blank=True)
    state = models.IntegerField(choices=PRINT_STATE, default=0)
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return "printer-" + str(self.id) + " : " + self.name

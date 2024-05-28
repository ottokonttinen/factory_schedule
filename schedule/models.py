from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Day(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.day.name} - {self.station.name} - {self.employee.name if self.employee else 'No Employee'}"

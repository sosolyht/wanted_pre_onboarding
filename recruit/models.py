from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'positions'

class Stack(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'stacks'


class Country(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'countries'


class State(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'states'


class Location(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        db_table = 'locations'


class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        db_table = 'companies'


class Recruit(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    compensation = models.IntegerField()
    content = models.TextField()
    stack = models.ForeignKey(Stack, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'recruits'
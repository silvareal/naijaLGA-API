from django.db import models


class State(models.Model):
    '''
    NG States api models
    '''
    state = models.CharField(max_length=20)
    capital = models.CharField(max_length=25)
    longitude = models.FloatField()
    latitude = models.FloatField()
    population = models.IntegerField()

    class Meta:
        ordering = ('-state', )

    def __str__(self):
        return self.state


class LGA(models.Model):
    '''
    Local government areas models
    '''
    state = models.ForeignKey(State , related_name='lga', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    longitude = models.FloatField()
    latitude = models.FloatField()
    population = models.IntegerField()

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name








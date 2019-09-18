from django.db import models


class Coord(models.Model):
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f'lon and lat'


class State(models.Model):
    '''
    NG States api models
    '''
    state = models.CharField(max_length=20)
    capital = models.CharField(max_length=25)
    population = models.IntegerField()
    coord = models.OneToOneField(Coord, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-state', )

    def __str__(self):
        return f'{self.state}'


class LGA(models.Model):
    '''
    Local government areas models
    '''
    state = models.ForeignKey(State, related_name='lga', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    population = models.IntegerField()
    coord = models.OneToOneField(Coord, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return f'{self.name}'

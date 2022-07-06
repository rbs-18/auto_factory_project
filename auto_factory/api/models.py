from django.db import models


class Parameter(models.Model):
    """ Model for parameters. """

    name = models.CharField('Наименование параметра', max_length=100)
    value = models.CharField('Значение параметра', max_length=50)


class Detail(models.Model):
    """ Model for details. """

    type_name = models.CharField('Тип детали', unique=True, max_length=40)
    price = models.FloatField('Стоимость детали')
    amount = models.IntegerField('Количество деталей на одну машину')
    parameters = models.ManyToManyField(Parameter, through='DetailParameter')


class DetailParameter(models.Model):
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)


class Cost(models.Model):
    """ Model for results. """

    prime_cost = models.FloatField('Себестоимость машины',)
    margin = models.CharField('Наценка', max_length=20)
    finall_price = models.FloatField('Финальная стоимость изделия')

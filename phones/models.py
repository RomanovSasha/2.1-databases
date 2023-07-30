from django.db import models


class Phone(models.Model):
    id = models.DecimalField(max_digits=10, decimal_places=2, primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.TextField()
    release_date = models.CharField(max_length=50)
    lte_exists = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    # TODO: Добавьте требуемые поля
    pass

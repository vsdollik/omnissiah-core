from django.db import models

class Blueprint(models.Model):
    type_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    max_runs = models.IntegerField(default=1)
    me = models.IntegerField(default=0)  # Material Efficiency
    te = models.IntegerField(default=0)  # Time Efficiency
    is_bpc = models.BooleanField(default=False)  # True если BPC, иначе BPO

    def __str__(self):
        return f"{self.name} (type_id={self.type_id})"

class Project(models.Model):
    name = models.CharField(max_length=255)
    product_type_id = models.IntegerField()
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32, default='planning')  # planning/production/complete

    def __str__(self):
        return f"{self.name} ({self.amount})"

from django.db import models

# Create your models here.


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=500)

    def __str__(self):
        return self.item_name

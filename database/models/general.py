from datetime import datetime

from tortoise.models import Model
from tortoise import fields

class MetricData(Model):
    id = fields.BigIntField(primary_key=True)
    date = fields.DateField()
    metric = fields.CharField(max_length=255)
    value = fields.FloatField()
    source: fields.ForeignKeyRelation[Source] = fields.ForeignKeyField("dw.Source")
    # device: fields.ForeignKeyRelation[Device] = fields.ForeignKeyField(
    #     "dw.Device", null=True
    # )
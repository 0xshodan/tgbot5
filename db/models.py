from tortoise.models import Model
from tortoise import fields



class User(Model):
    tgid = fields.BigIntField()
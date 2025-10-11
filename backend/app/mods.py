from tortoise import Model, fields


class Types(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    content = fields.TextField()

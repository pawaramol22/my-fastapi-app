import mongoengine as me


class Product(me.Document):
    meta = { "db": "myproducts", "collection": "products" }
    
    name = me.StringField(required=True)
    description = me.StringField()
    price = me.FloatField(required=True)

from database.db import db
import mongoengine_goodjson as gj


class Author(gj.Document):
    name = db.StringField(required=True, unique=True)

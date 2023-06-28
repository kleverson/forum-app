from forum.models.Base import Base
from forum.ext.database import db

class Forum(Base):
    name = db.Column(db.Text(), nullable=False)
    description =  db.Column(db.Text(), nullable=True)
    status = db.Column(db.Boolean, default=False)
    owner = db.Column(db.Integer, db.ForeignKey("user.id"))
    owner_id = db.relationship("User")

    def __init__(self, name, description, owner_id):
        self.name = name
        self.description = description
        self.owner = owner_id
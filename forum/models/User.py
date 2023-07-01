import binascii
import os
from itsdangerous import Serializer
from werkzeug.security import check_password_hash, generate_password_hash
from forum.models.Base import Base
from forum.ext.database import db


class User(Base):
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.Text())
    token = db.Column(db.String(32), default=None)
    active = db.Column(db.Boolean, default=False)

    def __init__(self, username, password, name, active):
        self.username = username
        self.password = generate_password_hash(password)
        self.name = name
        self.token = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
        self.active = active

    def serialize(cls):
        d = Serializer.serialize(cls)
        del d['password']
        return d

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    @classmethod
    def exists(cls, username):
        return cls.query.filter(User.username == username).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter(cls.username == username).first()

    @staticmethod
    def hash_pass(password):
        return generate_password_hash(password)

    @staticmethod
    def verify_hash(hash, password):
        return check_password_hash(hash, password)

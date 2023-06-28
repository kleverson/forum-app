from forum.models.Base import Base
from forum.ext.database import db
import enum

class ContentStatus(enum.Enum):
    OPEN ="OPEN"
    CLOSED = "CLOSED"

class TaxonomyType(enum.Enum):
    CATEGORY = "CATEGORY"
    TAG = "TAG"


class InteractionContent(db.Enum):
    VOTE="VOTE"
    LIKE="LIKE"

class Taxonomy(Base):
    title = db.Column(db.Text(), nullable=False)
    slug = db.Column(db.Text(), nullable=False)
    type = db.Column(db.Enum(TaxonomyType), nullable=True)
    parentId = db.Column(db.Integer, nullable=True, default = 0)

    def __init__(self, title, slug, type, parentId):
        self.title = title
        self.slug = slug
        self.type = type
        self.parentId = parentId

class Content(Base):
    title = db.Column(db.Text(), nullable=False)
    slug = db.Column(db.Text(), nullable=False)
    body =  db.Column(db.Text(), nullable=True)
    description =  db.Column(db.Text(), nullable=True)
    status = db.Column(db.Enum(ContentStatus), default=False)

    user = db.Column(db.Integer, db.ForeignKey("user.id"))
    user_id = db.relationship("User")

    def __init__(self, title, slug, body, description, status, user_id):
        self.title = title
        self.slug = slug
        self.body = body
        self.description = description
        self.status = status
        self.user_id = user_id

class ContentTaxonomy(Base):
    taxonomy = db.Column(db.Integer, db.ForeignKey("taxonomy.id"))
    taxonomy_id = db.relationship("Taxonomy")

    content = db.Column(db.Integer, db.ForeignKey("content.id"))
    content_id = db.relationship("Content")

    def __init__(self, category_id, content_id):
        self.category_id = category_id
        self.content_id = content_id

class ContentTagged(Base):
    content = db.Column(db.Integer, db.ForeignKey("content.id"))
    content_id = db.relationship("Content")

    user = db.Column(db.Integer, db.ForeignKey("user.id"))
    user_id = db.relationship("User")

    def __init__(self, content_id, user_id):
        self.content_id = content_id
        self.user_id = user_id

class ContentComment(Base):
    content = db.Column(db.Integer, db.ForeignKey("content.id"))
    content_id = db.relationship("Content")

    user = db.Column(db.Integer, db.ForeignKey("user.id"))
    user_id = db.relationship("User")

    description = db.Column(db.Text(), nullable=True)

    def __init__(self, content, user, description):
        self.content = content
        self.user = user
        self.description = description

class ContentInteraction(Base):
    content = db.Column(db.Integer, db.ForeignKey("content.id"))
    content_id = db.relationship("Content")

    user = db.Column(db.Integer, db.ForeignKey("user.id"))
    user_id = db.relationship("User")

    interaction = db.Column(db.Enum(InteractionContent), nullable=True)

    def __init__(self, content, user, description):
        self.content = content
        self.user = user
        self.interaction = description


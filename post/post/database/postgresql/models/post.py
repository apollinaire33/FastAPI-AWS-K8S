import uuid

from sqlalchemy import Column, String, Uuid, DateTime
from sqlalchemy.sql import func

from post.database.postgresql.setup_db import Base


class PostModel(Base):
    __tablename__ = "post"

    uuid = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    author_uuid = Column(Uuid(as_uuid=True))
    subject = Column(String(30))
    text = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

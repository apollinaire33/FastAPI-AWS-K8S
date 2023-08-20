import uuid

from sqlalchemy import Column, Integer, String, Uuid

from user.database.postgresql.setup_db import Base


class UserModel(Base):
    __tablename__ = "user"

    uuid = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(30))
    email = Column(String(30))
    age = Column(Integer)

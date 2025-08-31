from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column 
from sqlalchemy import UUID
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from uuid import uuid4

class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(pgUUID(as_uuid=True), default=uuid4, nullable=False)
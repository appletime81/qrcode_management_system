from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from config.db import Base


class Files(Base):
    __tablename__ = "file_management"
    id = Column(String(255), primary_key=True, index=True)
    server_ip = Column("server_ip", String(255), nullable=True)
    root_path = Column("root_path", String(255), nullable=True)
    file_name = Column("file_name", String(255), nullable=True)
    data_insert_date = Column("data_insert_date", DateTime, nullable=True)

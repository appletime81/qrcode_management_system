from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date
from config.db import meta

files = Table('file_management', meta,
              Column('server_ip', String(255), nullable=True),
              Column('root_path', String(255), nullable=True),
              Column('file_name', String(255), nullable=True),
              Column('data_insert_date', Date, nullable=True),
              )

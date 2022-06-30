from typing import List, Union, Optional
from datetime import datetime, date
from pydantic import BaseModel


class Files(BaseModel):
    server_ip: str
    root_path: str
    file_name: str
    data_insert_date: date

    class config:
        orm_mode = True
from typing import Optional
from sqlmodel import SQLModel, Field

class Link(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str
    url: str

from __future__ import annotations
from pydantic import BaseModel


class Data(BaseModel):
    name: str
    unique: str
    position: int | None = None
    sub_data: list[Data] = []
    is_new: bool = False
    updated: bool = False
    deleted: bool = False


class DataList(BaseModel):
    data: list[Data] = []

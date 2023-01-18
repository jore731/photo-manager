import typing
from datetime import datetime
from pathlib import Path
from uuid import UUID, uuid4

from PIL.Image import Image
from pydantic import BaseModel, Field


class Photo(BaseModel):
    path: Path = Field(title="path", description="UNIX path of file")
    id: UUID = Field(default_factory=uuid4)
    date: datetime = Field(default_factory=datetime.now)
    size: int = Field(title="size", description="Image size in bytes")
    image: typing.Any

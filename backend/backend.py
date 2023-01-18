from uuid import UUID

from fastapi import FastAPI
from model import Photo
from model.dao.PhotoDAO import ListPhotoDAO
from starlette.responses import FileResponse

photo_library: ListPhotoDAO = ListPhotoDAO()

app = FastAPI()


@app.post("/photos")
async def register_photos(photos: list[Photo]) -> list[Photo]:
    photo_library.create_photos(photos)
    return photo_library.get_all()


@app.get("/photos")
async def list_all() -> list[Photo]:
    return photo_library.get_all()


@app.post("/photo")
async def register_photo(photo: Photo) -> list[Photo]:
    photo_library.create_photo(photo)
    return photo_library.get_all()


@app.get("/photo/{photo_id}")
async def get_photo_file(photo_id: UUID) -> FileResponse:
    return FileResponse(photo_library.get_photo(photo_id).path)

from abc import ABC, abstractmethod
from uuid import UUID

from model import Photo


class PhotoDAO(ABC):
    def __init__(self):
        self.photos: dict[UUID, Photo] = {}

    @abstractmethod
    def get_photo(self, photo_id: UUID) -> Photo:
        pass

    @abstractmethod
    def create_photo(self, photo: Photo) -> None:
        pass

    @abstractmethod
    def create_photos(self, photos: list[Photo]) -> None:
        pass

    @abstractmethod
    def delete_photo(self, photo_id: UUID) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[Photo]:
        pass


class ListPhotoDAO(PhotoDAO):
    def get_photo(self, photo_id: UUID) -> Photo:
        return self.photos[photo_id]

    def create_photo(self, photo: Photo) -> None:
        self.photos[photo.id] = photo

    def create_photos(self, photos: list[Photo]) -> None:
        for photo in photos:
            self.create_photo(photo)

    def delete_photo(self, photo_id: UUID) -> None:
        del self.photos[photo_id]

    def get_all(self) -> list[Photo]:
        return list(self.photos.values())

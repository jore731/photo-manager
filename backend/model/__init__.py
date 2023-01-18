from .entity.Photo import Photo
from .dao.PhotoDAO import PhotoDAO, ListPhotoDAO

all([Photo, PhotoDAO, ListPhotoDAO])

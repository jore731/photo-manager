from pathlib import Path
from urllib.parse import urljoin

from PIL.Image import open
from requests import Session
from streamlit.runtime.uploaded_file_manager import UploadedFile

from model import Photo
import streamlit as st


class BackendConnector(Session):
    def __init__(self, base_url=None):
        super().__init__()
        self.base_url = base_url

    def request(self, method, url, *args, **kwargs):
        joined_url = urljoin(self.base_url, url)
        return super().request(method, joined_url, *args, **kwargs)


if 'connector' not in st.session_state:
    st.session_state['connector']: BackendConnector = BackendConnector("http://localhost:8000")

connector: BackendConnector = st.session_state['connector']
st.text("hey!")

data: list[UploadedFile] = st.file_uploader("Upload photos here!", accept_multiple_files=True)

for value in data:
    photo = Photo(path=value.name, size=value.size, image=open(value))
    response = connector.request("post", "/photo", data=photo.json())


photos: list[Photo] = list(map(lambda x: Photo(**x), connector.request("get", "/photos").json()))
print(photos)
for photo in photos:
    print(photo)
    photo_file = connector.request("get", f"/photo/{photo.id}")
    st.image(photo_file.content)

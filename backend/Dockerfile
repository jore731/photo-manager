FROM python:3.9-slim

ADD requirements.txt .

RUN pip install -r requirements.txt && rm requirements.txt

WORKDIR /app

COPY model model
COPY backend.py backend.py

EXPOSE 8000

CMD ["uvicorn", "backend:app", "--reload"]
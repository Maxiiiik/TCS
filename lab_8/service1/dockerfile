FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY service1.py .
# COPY field_centroids.geojson .

CMD ["python", "-u", "service1.py"]

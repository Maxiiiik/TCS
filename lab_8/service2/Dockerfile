FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY service2.py .


CMD [ "python", "-u", "service2.py" ]

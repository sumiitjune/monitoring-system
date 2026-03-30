FROM python:3.10-slim

WORKDIR /app

# install docker CLI
RUN apt-get update && apt-get install -y docker.io

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
 

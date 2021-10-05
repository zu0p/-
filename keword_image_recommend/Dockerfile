FROM python:3.6.8

COPY . .

RUN apt-get update && \
    apt-get install -y --no-install-recommends tzdata g++ git curl

# installing python3 and pip3
RUN apt-get install -y python3-pip python3-dev


RUN pip install -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8995"]

EXPOSE 8995
FROM python:3.9

EXPOSE 80

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:server", "--host", "0.0.0.0", "--port", "80"]

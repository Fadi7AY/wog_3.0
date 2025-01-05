FROM python:alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements

COPY Scores.txt /Scores.txt

EXPOSE 5000

CMD ["python", "app.py"]


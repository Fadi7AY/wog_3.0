
FROM python:3.9-slim
WORKDIR /app
COPY main_score.py /app
RUN pip install flask
COPY Scores.txt /Scores.txt
EXPOSE 5000
CMD ["python", "main_score.py"]

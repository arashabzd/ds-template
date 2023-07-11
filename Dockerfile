FROM python:latest

WORKDIR /app/project-name

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src src

CMD ["python", "src/main.py"]
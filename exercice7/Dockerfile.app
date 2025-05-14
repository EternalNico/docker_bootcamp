FROM python:3.9-slim
WORKDIR /app
COPY app/requirements.txt .
RUN pip install -r requirements.txt
COPY app/ .
EXPOSE 10011
CMD ["python", "app.py"]
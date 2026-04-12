FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
COPY requ requ

#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --no-index --find-links requ -r requirements.txt
RUN rm -R requ

COPY main.py .

EXPOSE 8081

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]

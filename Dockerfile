FROM python:3.10-slim
 
WORKDIR /app
 
COPY requirements.txt /app/requirements.txt
 
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
 
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app /app/app
COPY templates /app/templates
COPY static /app/static

RUN mkdir -p /app/templates /app/static

# Ensure template and static directories exist
RUN mkdir -p /app/templates /app/static
 
EXPOSE 8000
 
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--proxy-headers"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--proxy-headers"]
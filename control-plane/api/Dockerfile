FROM python:3.12-slim
WORKDIR /app
COPY control-plane/api/requirements.txt .
RUN pip install -r requirements.txt

# Copy source code to /app/src
COPY control-plane/api/src ./src

# Copy project template to /app/data-plane/project-template
# This bakes it into the image, so it's always available
COPY data-plane/project-template ./data-plane/project-template

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
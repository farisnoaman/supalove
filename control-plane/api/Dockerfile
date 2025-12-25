FROM python:3.12-slim
WORKDIR /app
# Install system dependencies including Docker CLI
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg \
    && echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && apt-get update && apt-get install -y docker-ce-cli docker-compose-plugin \
    && rm -rf /var/lib/apt/lists/*

COPY control-plane/api/requirements.txt .
RUN pip install -r requirements.txt

# Copy source code to /app/src
COPY control-plane/api/src ./src

# Copy project template to /app/data-plane/project-template
# This bakes it into the image, so it's always available
COPY data-plane/project-template ./data-plane/project-template

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
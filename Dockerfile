FROM mcr.microsoft.com/devcontainers/typescript-node:1-20

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /workspace

# Install app dependencies
COPY claude-office/package.json .
RUN npm install

# Copy backend
COPY claude-office/backend ./backend

# Install Python dependencies
RUN python3 -m pip install fastapi uvicorn sqlalchemy pydantic rich greenlet

# Expose ports
EXPOSE 8000 3000

# Start command
CMD ["bash", "-c", "echo 'Iniciando Claude Office...' && python3 -m uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 & npm run dev --turbo"]
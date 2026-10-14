FROM python:3.12-slim

WORKDIR /app

# Ensure non-buffered stdout for real-time logging in cloud dashboards
ENV PYTHONUNBUFFERED=1
ENV PORT=8080
ENV HOST=0.0.0.0
ENV ELYSIA_ALLOW_SERVER_EXEC=0

# Copy application codebase
COPY . /app

# Expose standard web port
EXPOSE 8080

# Run Elysia School production server
CMD ["python3", "main.py"]

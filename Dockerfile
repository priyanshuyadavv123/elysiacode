FROM python:3.12-slim

WORKDIR /app

# Ensure non-buffered stdout for real-time logging in cloud dashboards
ENV PYTHONUNBUFFERED=1
ENV PORT=8080
ENV HOST=0.0.0.0
ENV ELYSIA_ALLOW_SERVER_EXEC=0
ENV ELYSIA_TRUST_PROXY=1

# Copy application codebase
COPY . /app

# Expose standard web port
EXPOSE 8080

# Production container healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python3 -c "import urllib.request, os; urllib.request.urlopen('http://127.0.0.1:' + os.environ.get('PORT', '8080') + '/api/health')" || exit 1

# Run ElysiaCode production server
CMD ["python3", "main.py"]

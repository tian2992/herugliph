# Use the official lightweight Python image.
FROM python:3.9-slim

ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install -r /app/requirements.txt

CMD exec gunicorn --bind :$PORT  --log-level=info --workers 1 --threads 2 --timeout 0 app:app

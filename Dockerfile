FROM --platform=${BUILDPLATFORM:-linux/amd64} python:3.11.4-slim-buster as builder
RUN addgroup --system app && adduser --system --group app
ENV PYTHONUNBUFFERED 1

WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g'  /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY . /app

RUN chown -R app:app /app
USER app

# ENTRYPOINT ["/app/entrypoint.sh"]
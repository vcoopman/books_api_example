FROM python:3.8-buster
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["/bin/bash", "-c", "gunicorn --bind 0.0.0.0:8000 books:__hug_wsgi__"]
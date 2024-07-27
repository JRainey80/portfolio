FROM tiangolo/uwsgi-nginx:python3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV FLASK_ENV=production



FROM tiangolo/uwsgi-nginx:python3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

ENV FLASK_ENV=production

EXPOSE 80
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl -f http://localhost:80 || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"] 

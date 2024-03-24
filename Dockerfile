FROM tiangolo/uwsgi-nginx:python3.11

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY ./app.py /app

CMD ["flask", "run"]
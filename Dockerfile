FROM tiangolo/uwsgi-nginx:python3.11

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./app.py /app/

CMD ("flask", "run", "--host", "0.0.0.0")
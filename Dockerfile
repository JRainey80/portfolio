
WORKDIR /app

COPY ./requirements.txt /app
COPY . /app

RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
EXPOSE 80

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production


CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]

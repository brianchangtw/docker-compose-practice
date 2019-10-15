FROM python:3.7.4

COPY . /code

WORKDIR /code
RUN pip install -r requirements.txt
CMD gunicorn app:app -b 0.0.0.0:8080 --thread 5
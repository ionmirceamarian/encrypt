FROM python:3.7

RUN python --version
RUN pip --version

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY . ./
ENV FLASK_RUN_HOST 0.0.0.0

ENTRYPOINT ["uwsgi", "--socket", "0.0.0.0:5000", "--protocol=http", "-w", "wsgi:app"]

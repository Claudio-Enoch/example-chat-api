FROM python:3.9.2-slim

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV AWS_DEFAULT_REGION=us-west-2

# install requirements
RUN python -m pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY manage.py /src
COPY app /src/app
COPY tests /src/tests

CMD python manage.py run --host 0.0.0.0

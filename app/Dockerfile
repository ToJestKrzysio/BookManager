FROM python:3.10

ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR ./app/

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --system

COPY ./ ./

CMD python -m pip install --upgrade pip \
    && python manage.py migrate \
    && python mage.py runserver

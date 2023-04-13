FROM python:3.7.4-alpine3.10


ADD app/requirements.txt /app/requirements.txt

RUN set -ex \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt

ADD app /app
WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8801

CMD ["gunicorn", "--bind", ":8801", "--log-level", "debug", "--timeout", "120", "--workers", "3", "pilates.wsgi"]
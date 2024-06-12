FROM python:3.10-alpine3.20

ENV PYTHONUNBUFFERED 1
EXPOSE 8000

WORKDIR /usr/src/app

COPY requirements.txt .

COPY entrypoint.sh .


RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && chmod +x ./entrypoint.sh

COPY . .

ENTRYPOINT ["./entrypoint.sh"]
FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /backend

RUN pip install --upgrade pip

COPY . .

RUN pip install poetry

RUN make requirements

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY . /backend

EXPOSE 8000

CMD ["make", "run"]

FROM python:3.11-slim

RUN apt-get update && apt-get install

RUN python -m pip install --upgrade pip

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
EXPOSE 8008
CMD ["fastapi", "run", "app/main.py", "--port", "8008"]

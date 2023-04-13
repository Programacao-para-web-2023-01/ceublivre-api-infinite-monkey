FROM python:3.11

WORKDIR /app

COPY requriements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY main.py .

COPY ./src /app/src

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
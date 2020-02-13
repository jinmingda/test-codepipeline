FROM python:3.7-slim-buster

WORKDIR /app

COPY . .

RUN useradd -m sid && \
    chown -R sid:sid /app

USER sid

ENV PATH="/home/sid/.local/bin:${PATH}"

RUN pip install --user -r requirements/prod.txt

EXPOSE 8000

CMD ["gunicorn", "wsgi:application", "-wc", "gunicorn.py"]

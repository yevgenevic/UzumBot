FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r req.txt

CMD ["python", "root.py"]

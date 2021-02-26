FROM python:3.6

RUN mkdir -p /labs/lab1/app/
WORKDIR /labs/lab1/app/

COPY . /labs/lab1/app/
RUN pip install  --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python","start.py"]

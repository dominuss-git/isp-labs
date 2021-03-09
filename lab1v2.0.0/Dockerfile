FROM python:3.6
COPY ./requirements.txt ./labs/lab1/app/

# RUN mkdir -p /labs/lab1/app/
WORKDIR /labs/lab1/app/

RUN pip install  --no-cache-dir -r requirements.txt

COPY . /labs/lab1/app/


EXPOSE 8080

CMD ["python","start.py"]
FROM ubuntu

ADD ./app /app
WORKDIR /app

RUN apt-get update
RUN apt-get install python3-pip
RUN make

EXPOSE 5000

CMD ["python3", "app.py"]

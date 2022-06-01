FROM mysql:latest
COPY ./data/* /var/lib/mysql
RUN mkdir /test
COPY . /test
RUN echo "Copied"

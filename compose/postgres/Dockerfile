FROM postgres:15.4-alpine3.18

COPY ./compose/postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/* &&\
    mv /usr/local/bin/maintenance/* /usr/local/bin &&\
    rmdir /usr/local/bin/maintenance


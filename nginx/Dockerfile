FROM nginx:1.19.0-alpine

COPY ./certificate.crt /etc/nginx/ssl/certificate.crt
COPY ./private.key /etc/nginx/ssl/private.key

COPY ./default.conf /etc/nginx/conf.d/default.conf
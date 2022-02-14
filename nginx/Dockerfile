FROM nginx:1.19.0-alpine

COPY ./certificate.crt /etc/nginx/conf.d/certificate.crt
COPY ./private.key /etc/nginx/conf.d/private.key

COPY ./api.conf /etc/nginx/conf.d/api.conf
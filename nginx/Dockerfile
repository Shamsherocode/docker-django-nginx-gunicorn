FROM nginx:1.19.0-alpine

COPY ./cert.pem /etc/nginx/conf.d/cert.pem
COPY ./key.pem /etc/nginx/conf.d/key.pem

COPY ./api.conf /etc/nginx/conf.d/api.conf
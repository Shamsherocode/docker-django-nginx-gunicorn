FROM nginx:1.19.0-alpine

COPY  ./ca_bundle.crt /etc/nginx/ssl/certs/ca_bundle.crt
COPY  ./private.key /etc/nginx/ssl/private/private.key

COPY ./default.conf /etc/nginx/conf.d/default.conf
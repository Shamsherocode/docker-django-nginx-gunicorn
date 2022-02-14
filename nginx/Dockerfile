FROM nginx:1.19.0-alpine

COPY  ./ca_bundle.crt /etc/ssl/ca_bundle.crt
COPY  ./private.key /etc/ssl/private.key

COPY ./default.conf /etc/nginx/conf.d/default.conf
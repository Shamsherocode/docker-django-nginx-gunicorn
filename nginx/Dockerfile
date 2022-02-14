FROM nginx:1.19.0-alpine

COPY  ./ca_bundle.crt /etc/nginx/ssl/certs/ca_bundle.crt
COPY  ./private.key /etc/nginx/ssl/private/private.key

COPY ./letsencrypt /etc/

WORKDIR /etc/letsencrypt

CMD letsencrypt-auto certonly --standalone -d api.psd2htmlx.com

COPY ./default.conf /etc/nginx/conf.d/default.conf
FROM nginx:1.19.0-alpine

# COPY  ./ca_bundle.crt /etc/nginx/ssl/certs/ca_bundle.crt
# COPY  ./private.key /etc/nginx/ssl/private/private.key


# RUN sudo apt-get install certbot

# RUN apt-get install python3-certbot-nginx

CMD certbot --nginx -d api.psd2htmlx.com -d www.api.psd2htmlx.com

COPY ./api.psd2htmlx.com.conf /etc/nginx/conf.d/api.psd2htmlx.com.conf
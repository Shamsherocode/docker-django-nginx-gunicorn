FROM nginx:1.19.0-alpine

COPY ./cert.pem /etc/nginx/conf.d/cert.pem
COPY ./key.pem /etc/nginx/conf.d/key.pem

CMD openssl req -x509 -nodes -days 365 -subj "/C=CA/ST=QC/O=ocode, Inc./CN=api.psd2htmlx.com" -addext "subjectAltName=DNS:api.psd2htmlx.com" -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt;

COPY ./default.conf /etc/nginx/conf.d/default.conf
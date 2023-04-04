FROM ubuntu:latest
RUN apt-get update -y && apt-get install -y apache2
COPY web_server/ /var/www/html/
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]

# 1 Запустіть веб-сервер у Docker контейнері та зробіть його доступним на локальному порту:

## Додайте каталог web_server. У ньому створіть файл index.html із довільним контентом.

``` 
a
shuprr@Uplime:~$ cd web_server
shuprr@Uplime:~/web_server$ ls
index.html
```

## Створіть Dockerfile з базовим образом Ubuntu та необхідними залежностями.

```
b
FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y apache2

COPY web_server/ /var/www/html/

EXPOSE 80

CMD ["apache2ctl", "-D", "FOREGROUND"]
```


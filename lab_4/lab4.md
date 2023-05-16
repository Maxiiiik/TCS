
# docker-compose 

```
version: '3'
services:
  db:
    image: mysql:latest
    container_name: mysql
    restart: always
    environment:
      # MYSQL_ROOT_USER: root
      MYSQL_ROOT_PASSWORD: 'password'
      # MYSQL_DATABASE: test_db
      # MYSQL_ROOT_HOST: 'localhost' 
    ports:
      - "3306:3306"
    # volumes:
    #   - data:/var/lib/mysql
    #   -  "./mysql:/var/lib/mysql"
    #   -  "./mysql/my.cnf:/etc/mysql/my.cnf"

  phpmyadmin:
    image: phpmyadmin/phpmyadmin:latest
    container_name: phpmyadmin
    restart: always
    environment:
      PMA_HOST: 'db' 
      # PMA_USER: root
      # PMA_PASSWORD: password
      # PMA_ARBITRARY: 1
      
    ports:
      - "8080:80"
    # volumes:
    #   - ./config.inc.php:/etc/phpmyadmin/config.inc.php

#volumes:
 # data:
 ```
## docker-compose up -d
 ```
  shuprr@Uplime:~$ docker-compose up -d
  [+] Running 2/2
   ⠿ Container phpmyadmin  Running                                                                         0.0s
   ⠿ Container mysql       Started                                                                         1.8s
  shuprr@Uplime:~$ docker-compose ps
  NAME                IMAGE                          COMMAND                  SERVICE             CREATED             STATUS              PORTS
  mysql               mysql:latest                   "docker-entrypoint.s…"   db                  7 minutes ago       Up 7 minutes        0.0.0.0:3306->3306/tcp, 33060/tcp
  phpmyadmin          phpmyadmin/phpmyadmin:latest   "/docker-entrypoint.…"   phpmyadmin          8 minutes ago       Up 8 minutes        0.0.0.0:8080->80/tcp
 ```

 ## 1.png
 ![1](https://github.com/Maxiiiik/TCS/assets/63784207/c26c24f8-9220-47a9-9658-b3a8e5351c4b)

![he-hehe](https://user-images.githubusercontent.com/63784207/229834681-1aa48240-a289-46aa-a26a-0ad2c5e56054.gif)








# 4
## 4.png
![4](https://github.com/Maxiiiik/TCS/assets/63784207/29f8cfa3-e100-4fc6-a401-f9c74150ac87)

```
shuprr@Uplime:~/lab4$ docker-compose up -d
[+] Running 2/0
 ⠿ Container lab4-directory_service-1  Running                                                           0.0s
 ⠿ Container lab4-time_service-1       Running                                                           0.0s
shuprr@Uplime:~/lab4$ docker-compose logs
lab4-directory_service-1  | File: time_2023-05-02 22:31:38.txt, Content: 2023-05-02 22:31:38
lab4-directory_service-1  | File: time_2023-05-02 22:34:57.txt, Content: 2023-05-02 22:34:57
lab4-directory_service-1  | File: time_2023-05-02 22:32:08.txt, Content: 2023-05-02 22:32:08
lab4-directory_service-1  | File: time_2023-05-02 22:36:18.txt, Content: 2023-05-02 22:36:18
lab4-directory_service-1  | File: time_2023-05-02 22:32:38.txt, Content: 2023-05-02 22:32:38
lab4-directory_service-1  | File: time_2023-05-02 22:34:37.txt, Content: 2023-05-02 22:34:37
lab4-directory_service-1  | File: time_2023-05-02 22:32:28.txt, Content: 2023-05-02 22:32:28
lab4-directory_service-1  | File: time_2023-05-02 22:31:48.txt, Content: 2023-05-02 22:31:48
lab4-directory_service-1  | File: time_2023-05-02 22:32:18.txt, Content: 2023-05-02 22:32:18
lab4-directory_service-1  | File: time_2023-05-02 22:31:58.txt, Content: 2023-05-02 22:31:58
lab4-directory_service-1  | File: time_2023-05-02 22:34:47.txt, Content: 2023-05-02 22:34:47
lab4-directory_service-1  | File: time_2023-05-02 22:31:28.txt, Content: 2023-05-02 22:31:28
lab4-directory_service-1  | File: time_2023-05-02 22:35:07.txt, Content: 2023-05-02 22:35:07
lab4-directory_service-1  | File: time_2023-05-02 22:31:38.txt, Content: 2023-05-02 22:31:38
lab4-directory_service-1  | File: time_2023-05-02 22:34:57.txt, Content: 2023-05-02 22:34:57
lab4-directory_service-1  | File: time_2023-05-02 22:32:08.txt, Content: 2023-05-02 22:32:08
lab4-directory_service-1  | File: time_2023-05-02 22:36:18.txt, Content: 2023-05-02 22:36:18
lab4-directory_service-1  | File: time_2023-05-02 22:32:38.txt, Content: 2023-05-02 22:32:38
lab4-directory_service-1  | File: time_2023-05-02 22:34:37.txt, Content: 2023-05-02 22:34:37
``` 

``` 
shuprr@Uplime:~/lab4$ docker-compose ps
NAME                       IMAGE                    COMMAND                  SERVICE             CREATED             STATUS              PORTS
lab4-directory_service-1   lab4-directory_service   "python directory_se…"   directory_service   2 minutes ago       Up 2 minutes
lab4-time_service-1        lab4-time_service        "python time_service…"   time_service        2 minutes ago       Up 2 minutes
``` 


# 1 docker build -t myapp .
```
docker build -t myapp .
ERRO[0000] Can't add file /home/shuprr/.docker/run/docker-cli-api.sock to tar: archive/tar: sockets not supported
Sending build context to Docker daemon  32.26kB
Step 1/4 : FROM python:3
 ---> a8405b7e74cf
Step 2/4 : COPY app.py /
 ---> 3ceba1f832a9
Step 3/4 : RUN pip install flask
 ---> Running in 86f1653b0d84
Collecting flask
  Downloading Flask-2.2.3-py3-none-any.whl (101 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 101.8/101.8 kB 1.6 MB/s eta 0:00:00
Collecting Werkzeug>=2.2.2
  Downloading Werkzeug-2.2.3-py3-none-any.whl (233 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 233.6/233.6 kB 3.1 MB/s eta 0:00:00
Collecting Jinja2>=3.0
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.1/133.1 kB 5.7 MB/s eta 0:00:00
Collecting itsdangerous>=2.0
  Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Collecting click>=8.0
  Downloading click-8.1.3-py3-none-any.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.6/96.6 kB 5.8 MB/s eta 0:00:00
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.1.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (27 kB)
Installing collected packages: MarkupSafe, itsdangerous, click, Werkzeug, Jinja2, flask
Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.2 Werkzeug-2.2.3 click-8.1.3 flask-2.2.3 itsdangerous-2.1.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

[notice] A new release of pip available: 22.3.1 -> 23.0.1
[notice] To update, run: pip install --upgrade pip
Removing intermediate container 86f1653b0d84
 ---> 34ab9f454dfa
Step 4/4 : CMD [ "python", "./app.py" ]
 ---> Running in d234d5f5eed5
Removing intermediate container d234d5f5eed5
 ---> 4fb21a76144c
Successfully built 4fb21a76144c
Successfully tagged myapp:latest
```

# 2 docker run myapp
```
shuprr@Uplime:~$ docker run myapp
Hello, World! My name Max
```

```
shuprr@Uplime:~$ docker container ls -a
CONTAINER ID   IMAGE                        COMMAND                  CREATED         STATUS
   PORTS     NAMES
161b98d838b0   myapp                        "python ./app.py"        9 minutes ago   Exited (0) 9 minutes ago              elegant_nobel
c37cfdae7ec5   ellerbrock/alpine-bash-git   "/bin/bash"              2 hours ago     Exited (0) 47 minutes ago             lab1
ffdbe8c75430   ellerbrock/alpine-bash-git   "/usr/bin/dumb-init …"   2 hours ago     Exited (0) 2 hours ago                magical_noether
571bf8c88f7a   hello-world                  "/hello"                 2 hours ago     Exited (0) 2 hours ago                mystifying_ardinghelli
```



# 3 На вибраній мові програмування напишіть програму, яка зчитує текст цієї лабораторної роботи із файлу і виводить його у термінал.
```
PS C:\Edu\TCS\TCS\lab_2> & C:/Users/shupr/AppData/Local/Programs/Python/Python311/python.exe c:/Edu/TCS/TCS/lab_2/ap.py
hello world!
```

# 4 Створіть Dockerfile для запуску цієї програми у контейнері.
```
FROM python:3

COPY ap.py /
COPY labs2.txt /
RUN pip install flask
CMD ["python", "./ap.py"]
```


# 5 Створіть Dockerfile для запуску цієї програми у контейнері.
## 1
```
docker build -t myapp2 -f Dockerfile2 .
ERRO[0000] Can't add file /home/shuprr/.docker/run/docker-cli-api.sock to tar: archive/tar: sockets not supported
Sending build context to Docker daemon  35.33kB
Step 1/5 : FROM python:3
 ---> a8405b7e74cf
Step 2/5 : COPY ap.py /
 ---> c535950c0418
Step 3/5 : COPY labs2.txt /
 ---> c5c8504c4a12
Step 4/5 : RUN pip install flask
 ---> Running in 1e57393bc89e
Collecting flask
  Downloading Flask-2.2.3-py3-none-any.whl (101 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 101.8/101.8 kB 1.1 MB/s eta 0:00:00
Collecting Werkzeug>=2.2.2
  Downloading Werkzeug-2.2.3-py3-none-any.whl (233 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 233.6/233.6 kB 3.4 MB/s eta 0:00:00
Collecting Jinja2>=3.0
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.1/133.1 kB 4.2 MB/s eta 0:00:00
Collecting itsdangerous>=2.0
  Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Collecting click>=8.0
  Downloading click-8.1.3-py3-none-any.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.6/96.6 kB 4.9 MB/s eta 0:00:00
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.1.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (27 kB)
Installing collected packages: MarkupSafe, itsdangerous, click, Werkzeug, Jinja2, flask
Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.2 Werkzeug-2.2.3 click-8.1.3 flask-2.2.3 itsdangerous-2.1.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

[notice] A new release of pip available: 22.3.1 -> 23.0.1
[notice] To update, run: pip install --upgrade pip
Removing intermediate container 1e57393bc89e
 ---> 1463373865ee
Step 5/5 : CMD ["python", "./ap.py"]
 ---> Running in d373bb9c22ae
Removing intermediate container d373bb9c22ae
 ---> 12d8f3442f5b
Successfully built 12d8f3442f5b
Successfully tagged myapp2:latest
```

## 2
```
shuprr@Uplime:~$ docker run myapp2
hello world!
```

## 3
```
shuprr@Uplime:~$ docker container ls -a
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS
       PORTS     NAMES
f03762c3eb0f   myapp2                       "python ./ap.py"         59 seconds ago   Exited (0) 58 seconds ago                confident_almeida
161b98d838b0   myapp                        "python ./app.py"        37 minutes ago   Exited (0) 37 minutes ago                elegant_nobel
c37cfdae7ec5   ellerbrock/alpine-bash-git   "/bin/bash"              2 hours ago      Exited (0) About an hour ago             lab1
ffdbe8c75430   ellerbrock/alpine-bash-git   "/usr/bin/dumb-init …"   2 hours ago      Exited (0) 2 hours ago                   magical_noether
571bf8c88f7a   hello-world                  "/hello"                 3 hours ago      Exited (0) 3 hours ago                   mystifying_ardinghelli
```

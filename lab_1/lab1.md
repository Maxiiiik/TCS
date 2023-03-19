## 6.Задокументувати у файл результат запуску контейнера:


#1 hello-world
--------------------

```
shuprr@Uplime:~$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```

--------------------
#2 Задокументувати у файл результат запуску контейнера та його версію.
--------------------
```
shuprr@Uplime:~$ sudo docker images  hello-world
[sudo] password for shuprr:
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
hello-world   latest    feb5d9fea6a5   18 months ago   13.3kB
```

--------------------
#3 Запустити у контейнері alpine-bash-git інтерфейс командного рядка, задокументувати ім’я користувача, вміст кореневого каталогу системи та версію git.
--------------------
```
shuprr@Uplime:~$ docker pull ellerbrock/alpine-bash-git
Using default tag: latest
latest: Pulling from ellerbrock/alpine-bash-git
Digest: sha256:46262050f227c4515a501607873d760961ee32d92fa5b8cf9c89aca3c564d008
Status: Image is up to date for ellerbrock/alpine-bash-git:latest
docker.io/ellerbrock/alpine-bash-git:latest
```

--------------------
#4 Запустити у контейнері alpine-bash-git інтерфейс командного рядка, задокументувати ім’я користувача, вміст кореневого каталогу системи та версію git.
--------------------
```
1
shuprr@Uplime:~$ docker pull ellerbrock/alpine-bash-git
Using default tag: latest
latest: Pulling from ellerbrock/alpine-bash-git
Digest: sha256:46262050f227c4515a501607873d760961ee32d92fa5b8cf9c89aca3c564d008
Status: Image is up to date for ellerbrock/alpine-bash-git:latest
docker.io/ellerbrock/alpine-bash-git:latest
```

```
2
shuprr@Uplime:~$ docker run -it -d --name lab1 --entrypoint /bin/bash ellerbrock/alpine-bash-git
c37cfdae7ec51f31e22b11d1c8c7bce7f2327d53b8e938a0b6cc115d24cadc7b
```

```
3
shuprr@Uplime:~$ docker exec -it lab1 bash
bash-4.4$ exit
exit
```

```
4
shuprr@Uplime:/$ docker exec -it lab1 bash
bash-4.4$ ls
bash-4.4$ cd /
bash-4.4$ ls
bin    etc    lib    mnt    root   sbin   sys    usr
dev    home   media  proc   run    srv    tmp    var
```

```
5
bash-4.4$ git --version
git version 2.18.1
```


--------------------
#5 Склонувати у контейнер в домашній каталог користувача довільний репозиторій та задокументувати результат роботи команди і вміст домашнього каталогу.
--------------------
```
bash-4.4$ ls
bash-4.4$ cd home/download
bash-4.4$ ls
bash-4.4$ git clone https://github.com/Maxiiiik/repo.git
Cloning into 'repo'...
remote: Enumerating objects: 75, done.
remote: Counting objects: 100% (75/75), done.
remote: Compressing objects: 100% (43/43), done.
remote: Total 75 (delta 33), reused 54 (delta 22), pack-reused 0
Unpacking objects: 100% (75/75), done.
```

--------------------
#6 Вийти із поточного контейнера та перезапустити його. Запустити у контейнері командний рядок та задокументувати вміст домашнього каталогу після перезапуску.
--------------------
```
shuprr@Uplime:/$ docker restart lab1
lab1
shuprr@Uplime:/$ docker exec -it lab1 bash
bash-4.4$ ls
repo
bash-4.4$
```
# 1 Запустіть веб-сервер у Docker контейнері та зробіть його доступним на локальному порту:

## Додайте каталог web_server. У ньому створіть файл index.html із довільним контентом.

### a
``` 
shuprr@Uplime:~$ cd web_server
shuprr@Uplime:~/web_server$ ls
index.html
```

## Створіть Dockerfile з базовим образом Ubuntu та необхідними залежностями.

### b
```
FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y apache2

COPY web_server/ /var/www/html/

EXPOSE 80

CMD ["apache2ctl", "-D", "FOREGROUND"]
```


### C

#### 1 
```
shuprr@Uplime:~$ docker build -t web_server .
ERRO[0000] Can't add file /home/shuprr/.docker/run/docker-cli-api.sock to tar: archive/tar: sockets not supported
Sending build context to Docker daemon  40.96kB
Step 1/5 : FROM ubuntu:latest
 ---> 08d22c0ceb15
Step 2/5 : RUN apt-get update -y && apt-get install -y apache2
 ---> Running in 28bab022faf7
Get:1 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy InRelease [270 kB]
Get:3 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [869 kB]
Get:4 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [119 kB]
Get:5 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [905 kB]
Get:6 http://archive.ubuntu.com/ubuntu jammy-backports InRelease [107 kB]
Get:7 http://archive.ubuntu.com/ubuntu jammy/universe amd64 Packages [17.5 MB]
Get:8 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 Packages [829 kB]
Get:9 http://security.ubuntu.com/ubuntu jammy-security/multiverse amd64 Packages [23.2 kB]
Get:10 http://archive.ubuntu.com/ubuntu jammy/multiverse amd64 Packages [266 kB]
Get:11 http://archive.ubuntu.com/ubuntu jammy/restricted amd64 Packages [164 kB]
Get:12 http://archive.ubuntu.com/ubuntu jammy/main amd64 Packages [1792 kB]
Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1142 kB]
Get:14 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [1199 kB]
Get:15 http://archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [885 kB]
Get:16 http://archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 Packages [28.6 kB]
Get:17 http://archive.ubuntu.com/ubuntu jammy-backports/universe amd64 Packages [22.4 kB]
Get:18 http://archive.ubuntu.com/ubuntu jammy-backports/main amd64 Packages [49.0 kB]
Fetched 26.3 MB in 60s (440 kB/s)
Reading package lists...
Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
  apache2-bin apache2-data apache2-utils bzip2 ca-certificates file libapr1
  libaprutil1 libaprutil1-dbd-sqlite3 libaprutil1-ldap libbrotli1 libcurl4
  libexpat1 libgdbm-compat4 libgdbm6 libicu70 libjansson4 libldap-2.5-0
  libldap-common liblua5.3-0 libmagic-mgc libmagic1 libnghttp2-14 libperl5.34
  libpsl5 librtmp1 libsasl2-2 libsasl2-modules libsasl2-modules-db
  libsqlite3-0 libssh-4 libxml2 mailcap media-types mime-support netbase
  openssl perl perl-modules-5.34 publicsuffix ssl-cert xz-utils
Suggested packages:
  apache2-doc apache2-suexec-pristine | apache2-suexec-custom www-browser ufw
  bzip2-doc gdbm-l10n libsasl2-modules-gssapi-mit
  | libsasl2-modules-gssapi-heimdal libsasl2-modules-ldap libsasl2-modules-otp
  libsasl2-modules-sql perl-doc libterm-readline-gnu-perl
  | libterm-readline-perl-perl make libtap-harness-archive-perl
The following NEW packages will be installed:
  apache2 apache2-bin apache2-data apache2-utils bzip2 ca-certificates file
  libapr1 libaprutil1 libaprutil1-dbd-sqlite3 libaprutil1-ldap libbrotli1
  libcurl4 libexpat1 libgdbm-compat4 libgdbm6 libicu70 libjansson4
  libldap-2.5-0 libldap-common liblua5.3-0 libmagic-mgc libmagic1
  libnghttp2-14 libperl5.34 libpsl5 librtmp1 libsasl2-2 libsasl2-modules
  libsasl2-modules-db libsqlite3-0 libssh-4 libxml2 mailcap media-types
  mime-support netbase openssl perl perl-modules-5.34 publicsuffix ssl-cert
  xz-utils
0 upgraded, 43 newly installed, 0 to remove and 0 not upgraded.
Need to get 25.6 MB of archives.
After this operation, 111 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 perl-modules-5.34 all 5.34.0-3ubuntu1.1 [2976 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy/main amd64 libgdbm6 amd64 1.23-1 [33.9 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy/main amd64 libgdbm-compat4 amd64 1.23-1 [6606 B]
Get:4 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libperl5.34 amd64 5.34.0-3ubuntu1.1 [4819 kB]
Get:5 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 perl amd64 5.34.0-3ubuntu1.1 [232 kB]
Get:6 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libapr1 amd64 1.7.0-8ubuntu0.22.04.1 [108 kB]
Get:7 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libexpat1 amd64 2.4.7-1ubuntu0.2 [91.0 kB]
Get:8 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libaprutil1 amd64 1.6.1-5ubuntu4.22.04.1 [92.6 kB]
Get:9 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libsqlite3-0 amd64 3.37.2-2ubuntu0.1 [641 kB]
Get:10 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libaprutil1-dbd-sqlite3 amd64 1.6.1-5ubuntu4.22.04.1 [11.3 kB]
Get:11 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libsasl2-modules-db amd64 2.1.27+dfsg2-3ubuntu1.2 [20.5 kB]
Get:12 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libsasl2-2 amd64 2.1.27+dfsg2-3ubuntu1.2 [53.8 kB]
Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libldap-2.5-0 amd64 2.5.14+dfsg-0ubuntu0.22.04.1 [183 kB]
Get:14 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libaprutil1-ldap amd64 1.6.1-5ubuntu4.22.04.1 [9168 B]
Get:15 http://archive.ubuntu.com/ubuntu jammy/main amd64 libbrotli1 amd64 1.0.9-2build6 [315 kB]
Get:16 http://archive.ubuntu.com/ubuntu jammy/main amd64 libnghttp2-14 amd64 1.43.0-1build3 [76.3 kB]
Get:17 http://archive.ubuntu.com/ubuntu jammy/main amd64 libpsl5 amd64 0.21.0-1.2build2 [58.4 kB]
Get:18 http://archive.ubuntu.com/ubuntu jammy/main amd64 librtmp1 amd64 2.4+20151223.gitfa8646d.1-2build4 [58.2 kB]
Get:19 http://archive.ubuntu.com/ubuntu jammy/main amd64 libssh-4 amd64 0.9.6-2build1 [184 kB]
Get:20 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libcurl4 amd64 7.81.0-1ubuntu1.10 [290 kB]
Get:21 http://archive.ubuntu.com/ubuntu jammy/main amd64 libjansson4 amd64 2.13.1-1.1build3 [32.4 kB]
Get:22 http://archive.ubuntu.com/ubuntu jammy/main amd64 liblua5.3-0 amd64 5.3.6-1build1 [140 kB]
Get:23 http://archive.ubuntu.com/ubuntu jammy/main amd64 libicu70 amd64 70.1-2 [10.6 MB]
Get:24 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libxml2 amd64 2.9.13+dfsg-1ubuntu0.2 [764 kB]
Get:25 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 apache2-bin amd64 2.4.52-1ubuntu4.4 [1345 kB]
Get:26 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 apache2-data all 2.4.52-1ubuntu4.4 [165 kB]
Get:27 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 apache2-utils amd64 2.4.52-1ubuntu4.4 [89.5 kB]
Get:28 http://archive.ubuntu.com/ubuntu jammy/main amd64 media-types all 7.0.0 [25.5 kB]
Get:29 http://archive.ubuntu.com/ubuntu jammy/main amd64 mailcap all 3.70+nmu1ubuntu1 [23.8 kB]
Get:30 http://archive.ubuntu.com/ubuntu jammy/main amd64 mime-support all 3.66 [3696 B]
Get:31 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 apache2 amd64 2.4.52-1ubuntu4.4 [97.8 kB]
Get:32 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 openssl amd64 3.0.2-0ubuntu1.8 [1184 kB]
Get:33 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 ca-certificates all 20211016ubuntu0.22.04.1 [144 kB]
Get:34 http://archive.ubuntu.com/ubuntu jammy/main amd64 netbase all 6.3 [12.9 kB]
Get:35 http://archive.ubuntu.com/ubuntu jammy/main amd64 libmagic-mgc amd64 1:5.41-3 [257 kB]
Get:36 http://archive.ubuntu.com/ubuntu jammy/main amd64 libmagic1 amd64 1:5.41-3 [87.2 kB]
Get:37 http://archive.ubuntu.com/ubuntu jammy/main amd64 file amd64 1:5.41-3 [21.5 kB]
Get:38 http://archive.ubuntu.com/ubuntu jammy/main amd64 publicsuffix all 20211207.1025-1 [129 kB]
Get:39 http://archive.ubuntu.com/ubuntu jammy/main amd64 xz-utils amd64 5.2.5-2ubuntu1 [84.8 kB]
Get:40 http://archive.ubuntu.com/ubuntu jammy/main amd64 bzip2 amd64 1.0.8-5build1 [34.8 kB]
Get:41 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libldap-common all 2.5.14+dfsg-0ubuntu0.22.04.1 [15.9 kB]
Get:42 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 libsasl2-modules amd64 2.1.27+dfsg2-3ubuntu1.2 [68.8 kB]
Get:43 http://archive.ubuntu.com/ubuntu jammy/main amd64 ssl-cert all 1.1.2 [17.4 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 25.6 MB in 36s (705 kB/s)
Selecting previously unselected package perl-modules-5.34.
(Reading database ... 4395 files and directories currently installed.)
Preparing to unpack .../00-perl-modules-5.34_5.34.0-3ubuntu1.1_all.deb ...
Unpacking perl-modules-5.34 (5.34.0-3ubuntu1.1) ...
Selecting previously unselected package libgdbm6:amd64.
Preparing to unpack .../01-libgdbm6_1.23-1_amd64.deb ...
Unpacking libgdbm6:amd64 (1.23-1) ...
Selecting previously unselected package libgdbm-compat4:amd64.
Preparing to unpack .../02-libgdbm-compat4_1.23-1_amd64.deb ...
Unpacking libgdbm-compat4:amd64 (1.23-1) ...
Selecting previously unselected package libperl5.34:amd64.
Preparing to unpack .../03-libperl5.34_5.34.0-3ubuntu1.1_amd64.deb ...
Unpacking libperl5.34:amd64 (5.34.0-3ubuntu1.1) ...
Selecting previously unselected package perl.
Preparing to unpack .../04-perl_5.34.0-3ubuntu1.1_amd64.deb ...
Unpacking perl (5.34.0-3ubuntu1.1) ...
Selecting previously unselected package libapr1:amd64.
Preparing to unpack .../05-libapr1_1.7.0-8ubuntu0.22.04.1_amd64.deb ...
Unpacking libapr1:amd64 (1.7.0-8ubuntu0.22.04.1) ...
Selecting previously unselected package libexpat1:amd64.
Preparing to unpack .../06-libexpat1_2.4.7-1ubuntu0.2_amd64.deb ...
Unpacking libexpat1:amd64 (2.4.7-1ubuntu0.2) ...
Selecting previously unselected package libaprutil1:amd64.
Preparing to unpack .../07-libaprutil1_1.6.1-5ubuntu4.22.04.1_amd64.deb ...
Unpacking libaprutil1:amd64 (1.6.1-5ubuntu4.22.04.1) ...
Selecting previously unselected package libsqlite3-0:amd64.
Preparing to unpack .../08-libsqlite3-0_3.37.2-2ubuntu0.1_amd64.deb ...
Unpacking libsqlite3-0:amd64 (3.37.2-2ubuntu0.1) ...
Selecting previously unselected package libaprutil1-dbd-sqlite3:amd64.
Preparing to unpack .../09-libaprutil1-dbd-sqlite3_1.6.1-5ubuntu4.22.04.1_amd64.deb ...
Unpacking libaprutil1-dbd-sqlite3:amd64 (1.6.1-5ubuntu4.22.04.1) ...
Selecting previously unselected package libsasl2-modules-db:amd64.
Preparing to unpack .../10-libsasl2-modules-db_2.1.27+dfsg2-3ubuntu1.2_amd64.deb ...
Unpacking libsasl2-modules-db:amd64 (2.1.27+dfsg2-3ubuntu1.2) ...
Selecting previously unselected package libsasl2-2:amd64.
Preparing to unpack .../11-libsasl2-2_2.1.27+dfsg2-3ubuntu1.2_amd64.deb ...
Unpacking libsasl2-2:amd64 (2.1.27+dfsg2-3ubuntu1.2) ...
Selecting previously unselected package libldap-2.5-0:amd64.
Preparing to unpack .../12-libldap-2.5-0_2.5.14+dfsg-0ubuntu0.22.04.1_amd64.deb ...
Unpacking libldap-2.5-0:amd64 (2.5.14+dfsg-0ubuntu0.22.04.1) ...
Selecting previously unselected package libaprutil1-ldap:amd64.
Preparing to unpack .../13-libaprutil1-ldap_1.6.1-5ubuntu4.22.04.1_amd64.deb ...
Unpacking libaprutil1-ldap:amd64 (1.6.1-5ubuntu4.22.04.1) ...
Selecting previously unselected package libbrotli1:amd64.
Preparing to unpack .../14-libbrotli1_1.0.9-2build6_amd64.deb ...
Unpacking libbrotli1:amd64 (1.0.9-2build6) ...
Selecting previously unselected package libnghttp2-14:amd64.
Preparing to unpack .../15-libnghttp2-14_1.43.0-1build3_amd64.deb ...
Unpacking libnghttp2-14:amd64 (1.43.0-1build3) ...
Selecting previously unselected package libpsl5:amd64.
Preparing to unpack .../16-libpsl5_0.21.0-1.2build2_amd64.deb ...
Unpacking libpsl5:amd64 (0.21.0-1.2build2) ...
Selecting previously unselected package librtmp1:amd64.
Preparing to unpack .../17-librtmp1_2.4+20151223.gitfa8646d.1-2build4_amd64.deb ...
Unpacking librtmp1:amd64 (2.4+20151223.gitfa8646d.1-2build4) ...
Selecting previously unselected package libssh-4:amd64.
Preparing to unpack .../18-libssh-4_0.9.6-2build1_amd64.deb ...
Unpacking libssh-4:amd64 (0.9.6-2build1) ...
Selecting previously unselected package libcurl4:amd64.
Preparing to unpack .../19-libcurl4_7.81.0-1ubuntu1.10_amd64.deb ...
Unpacking libcurl4:amd64 (7.81.0-1ubuntu1.10) ...
Selecting previously unselected package libjansson4:amd64.
Preparing to unpack .../20-libjansson4_2.13.1-1.1build3_amd64.deb ...
Unpacking libjansson4:amd64 (2.13.1-1.1build3) ...
Selecting previously unselected package liblua5.3-0:amd64.
Preparing to unpack .../21-liblua5.3-0_5.3.6-1build1_amd64.deb ...
Unpacking liblua5.3-0:amd64 (5.3.6-1build1) ...
Selecting previously unselected package libicu70:amd64.
Preparing to unpack .../22-libicu70_70.1-2_amd64.deb ...
Unpacking libicu70:amd64 (70.1-2) ...
Selecting previously unselected package libxml2:amd64.
Preparing to unpack .../23-libxml2_2.9.13+dfsg-1ubuntu0.2_amd64.deb ...
Unpacking libxml2:amd64 (2.9.13+dfsg-1ubuntu0.2) ...
Selecting previously unselected package apache2-bin.
Preparing to unpack .../24-apache2-bin_2.4.52-1ubuntu4.4_amd64.deb ...
Unpacking apache2-bin (2.4.52-1ubuntu4.4) ...
Selecting previously unselected package apache2-data.
Preparing to unpack .../25-apache2-data_2.4.52-1ubuntu4.4_all.deb ...
Unpacking apache2-data (2.4.52-1ubuntu4.4) ...
Selecting previously unselected package apache2-utils.
Preparing to unpack .../26-apache2-utils_2.4.52-1ubuntu4.4_amd64.deb ...
Unpacking apache2-utils (2.4.52-1ubuntu4.4) ...
Selecting previously unselected package media-types.
Preparing to unpack .../27-media-types_7.0.0_all.deb ...
Unpacking media-types (7.0.0) ...
Selecting previously unselected package mailcap.
Preparing to unpack .../28-mailcap_3.70+nmu1ubuntu1_all.deb ...
Unpacking mailcap (3.70+nmu1ubuntu1) ...
Selecting previously unselected package mime-support.
Preparing to unpack .../29-mime-support_3.66_all.deb ...
Unpacking mime-support (3.66) ...
Selecting previously unselected package apache2.
Preparing to unpack .../30-apache2_2.4.52-1ubuntu4.4_amd64.deb ...
Unpacking apache2 (2.4.52-1ubuntu4.4) ...
Selecting previously unselected package openssl.
Preparing to unpack .../31-openssl_3.0.2-0ubuntu1.8_amd64.deb ...
Unpacking openssl (3.0.2-0ubuntu1.8) ...
Selecting previously unselected package ca-certificates.
Preparing to unpack .../32-ca-certificates_20211016ubuntu0.22.04.1_all.deb ...
Unpacking ca-certificates (20211016ubuntu0.22.04.1) ...
Selecting previously unselected package netbase.
Preparing to unpack .../33-netbase_6.3_all.deb ...
Unpacking netbase (6.3) ...
Selecting previously unselected package libmagic-mgc.
Preparing to unpack .../34-libmagic-mgc_1%3a5.41-3_amd64.deb ...
Unpacking libmagic-mgc (1:5.41-3) ...
Selecting previously unselected package libmagic1:amd64.
Preparing to unpack .../35-libmagic1_1%3a5.41-3_amd64.deb ...
Unpacking libmagic1:amd64 (1:5.41-3) ...
Selecting previously unselected package file.
Preparing to unpack .../36-file_1%3a5.41-3_amd64.deb ...
Unpacking file (1:5.41-3) ...
Selecting previously unselected package publicsuffix.
Preparing to unpack .../37-publicsuffix_20211207.1025-1_all.deb ...
Unpacking publicsuffix (20211207.1025-1) ...
Selecting previously unselected package xz-utils.
Preparing to unpack .../38-xz-utils_5.2.5-2ubuntu1_amd64.deb ...
Unpacking xz-utils (5.2.5-2ubuntu1) ...
Selecting previously unselected package bzip2.
Preparing to unpack .../39-bzip2_1.0.8-5build1_amd64.deb ...
Unpacking bzip2 (1.0.8-5build1) ...
Selecting previously unselected package libldap-common.
Preparing to unpack .../40-libldap-common_2.5.14+dfsg-0ubuntu0.22.04.1_all.deb ...
Unpacking libldap-common (2.5.14+dfsg-0ubuntu0.22.04.1) ...
Selecting previously unselected package libsasl2-modules:amd64.
Preparing to unpack .../41-libsasl2-modules_2.1.27+dfsg2-3ubuntu1.2_amd64.deb ...
Unpacking libsasl2-modules:amd64 (2.1.27+dfsg2-3ubuntu1.2) ...
Selecting previously unselected package ssl-cert.
Preparing to unpack .../42-ssl-cert_1.1.2_all.deb ...
Unpacking ssl-cert (1.1.2) ...
Setting up libexpat1:amd64 (2.4.7-1ubuntu0.2) ...
Setting up media-types (7.0.0) ...
Setting up libpsl5:amd64 (0.21.0-1.2build2) ...
Setting up libmagic-mgc (1:5.41-3) ...
Setting up libbrotli1:amd64 (1.0.9-2build6) ...
Setting up libsqlite3-0:amd64 (3.37.2-2ubuntu0.1) ...
Setting up libsasl2-modules:amd64 (2.1.27+dfsg2-3ubuntu1.2) ...
Setting up libnghttp2-14:amd64 (1.43.0-1build3) ...
Setting up libmagic1:amd64 (1:5.41-3) ...
Setting up libapr1:amd64 (1.7.0-8ubuntu0.22.04.1) ...
Setting up file (1:5.41-3) ...
Setting up perl-modules-5.34 (5.34.0-3ubuntu1.1) ...
Setting up bzip2 (1.0.8-5build1) ...
Setting up libldap-common (2.5.14+dfsg-0ubuntu0.22.04.1) ...
Setting up libjansson4:amd64 (2.13.1-1.1build3) ...
Setting up libsasl2-modules-db:amd64 (2.1.27+dfsg2-3ubuntu1.2) ...
Setting up librtmp1:amd64 (2.4+20151223.gitfa8646d.1-2build4) ...
Setting up xz-utils (5.2.5-2ubuntu1) ...
update-alternatives: using /usr/bin/xz to provide /usr/bin/lzma (lzma) in auto mode
update-alternatives: warning: skip creation of /usr/share/man/man1/lzma.1.gz because associated file /usr/share/man/man1/xz.1.gz (of link group lzma) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/unlzma.1.gz because associated file /usr/share/man/man1/unxz.1.gz (of link group lzma) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/lzcat.1.gz because associated file /usr/share/man/man1/xzcat.1.gz (of link group lzma) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/lzmore.1.gz because associated file /usr/share/man/man1/xzmore.1.gz (of link group lzma) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/lzless.1.gz because associated file /usr/share/man/man1/xzless.1.gz (of link group lzma) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/lzdiff.1.gz because associated file /usr/share/man/man1/xzdiff.1.gz (of link group lzma) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/lzcmp.1.gz because associated file /usr/share/man/man1/xzcmp.1.gz (of link group lzma) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/lzgrep.1.gz because associated file /usr/share/man/man1/xzgrep.1.gz (of link group lzma) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/lzegrep.1.gz because associated file /usr/share/man/man1/xzegrep.1.gz (of link group lzma) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/lzfgrep.1.gz because associated file /usr/share/man/man1/xzfgrep.1.gz (of link group lzma) doesn't exist
Setting up libsasl2-2:amd64 (2.1.27+dfsg2-3ubuntu1.2) ...
Setting up libssh-4:amd64 (0.9.6-2build1) ...
Setting up liblua5.3-0:amd64 (5.3.6-1build1) ...
Setting up netbase (6.3) ...
Setting up apache2-data (2.4.52-1ubuntu4.4) ...
Setting up openssl (3.0.2-0ubuntu1.8) ...
Setting up publicsuffix (20211207.1025-1) ...
Setting up libgdbm6:amd64 (1.23-1) ...
Setting up libicu70:amd64 (70.1-2) ...
Setting up libaprutil1:amd64 (1.6.1-5ubuntu4.22.04.1) ...
Setting up libaprutil1-dbd-sqlite3:amd64 (1.6.1-5ubuntu4.22.04.1) ...
Setting up libldap-2.5-0:amd64 (2.5.14+dfsg-0ubuntu0.22.04.1) ...
Setting up ca-certificates (20211016ubuntu0.22.04.1) ...
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline
Updating certificates in /etc/ssl/certs...
124 added, 0 removed; done.
Setting up ssl-cert (1.1.2) ...
debconf: unable to initialize frontend: Dialog
debconf: (TERM is not set, so the dialog frontend is not usable.)
debconf: falling back to frontend: Readline
Setting up libgdbm-compat4:amd64 (1.23-1) ...
Setting up libcurl4:amd64 (7.81.0-1ubuntu1.10) ...
Setting up libxml2:amd64 (2.9.13+dfsg-1ubuntu0.2) ...
Setting up apache2-utils (2.4.52-1ubuntu4.4) ...
Setting up libperl5.34:amd64 (5.34.0-3ubuntu1.1) ...
Setting up libaprutil1-ldap:amd64 (1.6.1-5ubuntu4.22.04.1) ...
Setting up perl (5.34.0-3ubuntu1.1) ...
Setting up mailcap (3.70+nmu1ubuntu1) ...
Setting up mime-support (3.66) ...
Setting up apache2-bin (2.4.52-1ubuntu4.4) ...
Setting up apache2 (2.4.52-1ubuntu4.4) ...
Enabling module mpm_event.
Enabling module authz_core.
Enabling module authz_host.
Enabling module authn_core.
Enabling module auth_basic.
Enabling module access_compat.
Enabling module authn_file.
Enabling module authz_user.
Enabling module alias.
Enabling module dir.
Enabling module autoindex.
Enabling module env.
Enabling module mime.
Enabling module negotiation.
Enabling module setenvif.
Enabling module filter.
Enabling module deflate.
Enabling module status.
Enabling module reqtimeout.
Enabling conf charset.
Enabling conf localized-error-pages.
Enabling conf other-vhosts-access-log.
Enabling conf security.
Enabling conf serve-cgi-bin.
Enabling site 000-default.
invoke-rc.d: could not determine current runlevel
invoke-rc.d: policy-rc.d denied execution of start.
Processing triggers for libc-bin (2.35-0ubuntu3.1) ...
Processing triggers for ca-certificates (20211016ubuntu0.22.04.1) ...
Updating certificates in /etc/ssl/certs...
0 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d...
done.
Removing intermediate container 28bab022faf7
 ---> 215a9d9e29df
Step 3/5 : COPY web_server/ /var/www/html/
 ---> 1eaa3784c3a7
Step 4/5 : EXPOSE 80
 ---> Running in 373ee88b1c4a
Removing intermediate container 373ee88b1c4a
 ---> e3b93ec4b374
Step 5/5 : CMD ["apache2ctl", "-D", "FOREGROUND"]
 ---> Running in a57748232448
Removing intermediate container a57748232448
 ---> ac7316592b3f
Successfully built ac7316592b3f
Successfully tagged web_server:latest
```

#### 2
```
shuprr@Uplime:~$ docker run -p 8080:80 -v /path/to/server:/var/www/html/ webapp
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' directive globally to suppress this message
```

### d,e  Перевірте доступність веб-сервера за адресою http://localhost:8080
```
1.png
```

# 2 Запустити базу даних MySQL та PHPMyAdmin у Docker контейнерах та зробити їх доступними на локальному порту.


## Створіть папку "mysql" та файл "my.cnf" з наступним вмістом:

### a 
```
[mysqld]
skip-host-cache
skip-name-resolve
```

## Створіть папку "mysql" та файл "my.cnf" з наступним вмістом:

### b 
```
shuprr@Uplime:~$ docker pull mysql/mysql-server:latest
latest: Pulling from mysql/mysql-server
6a4a3ef82cdc: Pull complete
5518b09b1089: Pull complete
b6b576315b62: Pull complete
349b52643cc3: Pull complete
abe8d2406c31: Pull complete
c7668948e14a: Pull complete
c7e93886e496: Pull complete
Digest: sha256:d6c8301b7834c5b9c2b733b10b7e630f441af7bc917c74dba379f24eeeb6a313
Status: Downloaded newer image for mysql/mysql-server:latest
```

## Запустіть контейнер зі змонтованим конфігураційним файлом та прокинутим портом 3306

### c
```
shuprr@Uplime:~$ docker run -d -p 3306:3306 --name=mysql -v $(pwd)/mysql:/etc/mysql/conf.d -v $(pwd)/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=password mysql/mysql-server:latest
1c0ee4df017d96437372c133beb8b15a8b707339ff56ffdcb93082699f06ee0f
```

## Завантажте образ PHPMyAdmin з Docker Hub.

### d 
```
shuprr@Uplime:~$ docker pull phpmyadmin/phpmyadmin:latest
latest: Pulling from phpmyadmin/phpmyadmin
01b5b2efb836: Pull complete
45244a9928d1: Pull complete
139d4815e950: Pull complete
9a420fd884ad: Pull complete
1de46a46cfcd: Pull complete
9cc46e699e97: Pull complete
9a8d67ebc9db: Pull complete
f9464a3489e8: Pull complete
5fececf0d356: Pull complete
6dd28e697cc8: Pull complete
b38a56ab5f21: Pull complete
ca91e5a7ae8b: Pull complete
185f934955ec: Pull complete
a077202948ae: Pull complete
1f511389296f: Pull complete
335d8ddb8d9f: Pull complete
68f3e41ea3a9: Pull complete
a28d69dfa6d4: Pull complete
Digest: sha256:0d951ee3bec76c5d7083122f5db509ebfa6c209efc5e70f1d47af2e13a34f543
Status: Downloaded newer image for phpmyadmin/phpmyadmin:latest
docker.io/phpmyadmin/phpmyadmin:latest
```

## Запустіть контейнер PHPMyAdmin зі змонтованою папкою "config" та прокинутим портом 8080.

### e 
```
shuprr@Uplime:~$ docker run -d --name myadmin -v ~/config.inc.php:/etc/phpmyadmin/config.inc.php -e PMA_HOST=localhost -p 8080:80 phpmyadmin/phpmyadmin:latest
154245a34dae10c650d36bd1926bd642164b35312cd239546d2bf59296324018
```

```
shuprr@Uplime:~$ docker ps
CONTAINER ID   IMAGE                          COMMAND                  CREATED          STATUS                    PORTS                                     NAMES
154245a34dae   phpmyadmin/phpmyadmin:latest   "/docker-entrypoint.…"   10 minutes ago   Up 10 minutes             0.0.0.0:8080->80/tcp                      myadmin
9334b8297c57   mysql/mysql-server:latest      "/entrypoint.sh mysq…"   29 minutes ago   Up 29 minutes (healthy)   0.0.0.0:3306->3306/tcp, 33060-33061/tcp   mysql
```

## Перейдіть за адресою http://localhost:8080 у веб-браузері та введіть логін та пароль для доступу до бази даних.
## Додайте у каталог скріншот запущеного PHPMyAdmin із відкритим списком таблиць бази даних MySQL.

### f,g 
```
2.png

Помилка...
mysqli::real_connect(): (HY000/2002): No such file or directory
```

# Можливо в завданні самому помилка, але з терміналу воно заходить(в самому Docker`i root password) 
```
3.png

sh-4.4# mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 20
Server version: 8.0.32 MySQL Community Server - GPL

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

```
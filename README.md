(venv) ubuntu@ubuntu:~/workspace/mariadb-demo$ sudo mysql -u project_user -p
[sudo] password for ubuntu:
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 63
Server version: 10.11.8-MariaDB-0ubuntu0.24.04.1 Ubuntu 24.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE DATABASE school;
Query OK, 1 row affected (0.001 sec)

MariaDB [(none)]> USE school;
Database changed
MariaDB [school]>
MariaDB [school]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| phpmyadmin         |
| school             |
| sys                |
| your_database      |
+--------------------+
7 rows in set (0.002 sec)

MariaDB [school]>

#!/bin/bash

export DEBIAN_FRONTEND="noninteractive"

sudo apt-get -y update && apt-get install -y apache2 apache2-doc apache2-utils mysql-server php libapache2-mod-php php-mcrypt php-mysql python

#sudo mkdir /var/www/html/images
sudo cp /home/vagrant/html/* /var/www/html

export APACHE_RUN_USER=www-data
export APACHE_RUN_GROUP=www-data
export APACHE_PID_FILE=/var/run/apache2.pid
export APACHE_RUN_DIR=/var/run/apache2
export APACHE_LOCK_DIR=/var/lock/apache2
export APACHE_LOG_DIR=/var/log/apache2

sudo service mysql start && mysql -uroot -e "CREATE DATABASE SqliDB; CREATE USER 'sqli-server'@'localhost' IDENTIFIED BY 'Bx117@\$YaML**\!'; GRANT ALL PRIVILEGES ON SqliDB.* TO 'sqli-server'@'localhost'; USE SqliDB; CREATE TABLE Users (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, User varchar(20), Password varchar(100)); INSERT INTO Users (User,Password) VALUES ('admin','wEareTHeAggIE$TheAggiesAReW3'); INSERT INTO Users (User,Password) VALUES ('bob','bobspassword'); SET PASSWORD FOR root@'localhost' = PASSWORD('Tl6@$0lxyaA@#--Jl3NMA@1-9283D')";

sudo service apache2 restart;

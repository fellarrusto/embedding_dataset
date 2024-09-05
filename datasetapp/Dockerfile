FROM php:8.0-apache

# Installazione dell'estensione pdo_mysql
RUN docker-php-ext-install pdo pdo_mysql

# Copia il codice dell'app nella cartella corretta di Apache
COPY . /var/www/html/

# Abilita i moduli Apache necessari
RUN a2enmod rewrite

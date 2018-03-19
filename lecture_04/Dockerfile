# https://www.unixmen.com/install-apache-ssl-ubuntu-13-10/
# https://www.itzgeek.com/how-tos/linux/linux-mint-how-tos/install-apache-web-server-on-linux-mint-13-linux-mint-14.html

FROM linuxmintd/mint19-amd64

run apt-get update
run apt-get install -y apache2 apache2-doc apache2-utils
run apt-get install -y vim

run mkdir /etc/apache2/ssl
run mkdir /var/www/html/example
run rm /var/www/html/index.html

add dockerfiles/server.key /etc/apache2/ssl/apache.key
add dockerfiles/server.crt /etc/apache2/ssl/apache.crt
add dockerfiles/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
add dockerfiles/index.html /var/www/html/example/index.html

run a2enmod ssl
run a2ensite default-ssl

WORKDIR /bsk
ADD . /bsk

EXPOSE 80
EXPOSE 443

CMD ["/bin/bash"]


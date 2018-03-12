# this file is based on: https://docs.docker.com/engine/examples/running_ssh_service/#build-an-eg_sshd-image
# and http://ubuntuguide.net/install-and-enable-telnet-server-in-ubuntu-linux
FROM linuxmintd/mint19-amd64

run apt-get update
run apt-get install -y openssh-client openssh-server vim telnet telnetd
run apt-get install -y xinetd
run mkdir -p /home/bsk
run mkdir /var/run/sshd

run useradd -d /home/bsk -p bsk -s /bin/bash bsk
run echo 'bsk:bardzotajnehaslo' | chpasswd
run echo 'root:root' | chpasswd

WORKDIR /

EXPOSE 22
EXPOSE 23
EXPOSE 12345

CMD ["/bin/bash"]


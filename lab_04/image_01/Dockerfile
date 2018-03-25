FROM linuxmintd/mint19-amd64

run apt-get update
run apt-get install -y openssh-client openssh-server vim python3-pip
run pip3 install -U pip
run pip3 install -U setuptools
run pip3 install -U cryptography
run pip3 install -U pyopenssl

run mkdir -p /home/bsk
run mkdir /var/run/sshd

run useradd -d /home/bsk -p bsk -s /bin/bash bsk
run echo 'bsk:bardzotajnehaslo' | chpasswd
run echo 'root:root' | chpasswd

WORKDIR /

EXPOSE 22

CMD ["/bin/bash"]


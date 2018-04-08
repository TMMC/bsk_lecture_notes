FROM linuxmintd/mint19-amd64

run apt-get update
run apt-get install -y vim lynx links openvpn openssh-server 

expose 22
expose 80
expose 12345

CMD ["/bin/bash"]


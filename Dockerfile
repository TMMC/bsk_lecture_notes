FROM linuxmintd/mint19-amd64

run apt-get update
run apt-get install -y vim gnupg2 

# https://d.sb/2016/11/gpg-inappropriate-ioctl-for-device-errors
run gpg --list-keys
run echo "use-agent" >> ~/.gnupg/gpg.conf
run echo "pinentry-mode loopback" >> ~/.gnupg/gpg.conf
run echo "allow-loopback-pinentry" >>  ~/.gnupg/gpg-agent.conf


add dockerfiles/bsk.key bsk.key
add dockerfiles/test.key test.key
add dockerfiles/message1.asc message1.asc
add dockerfiles/message2.asc message2.asc

# https://unix.stackexchange.com/questions/60213/gpg-asks-for-password-even-with-passphrase
run gpg --batch --yes --passphrase bsk --import bsk.key

EXPOSE 22

CMD ["/bin/bash"]


FROM linuxmintd/mint19-amd64

run apt-get update
run apt-get install -y apt-utils
run apt-get install -y build-essential libssl-dev git
run apt-get install -y yasm libgmp-dev libpcap-dev pkg-config libbz2-dev

run mkdir /apps
WORKDIR /apps
run git clone git://github.com/magnumripper/JohnTheRipper -b bleeding-jumbo john
WORKDIR /apps/john/src
run ./configure && make -s clean && make -sj4
workdir /apps/john/run
run touch john-local.conf
workdir /apps
run wget http://project-rainbowcrack.com/rainbowcrack-1.7-linux64.zip
run unzip rainbowcrack-1.7-linux64.zip
run mv rainbowcrack-1.7-linux64 rainbowcrack
run rm rainbowcrack-1.7-linux64.zip
workdir /apps/rainbowcrack
run chmod a+x rt*
run chmod a+x rc*

WORKDIR /bsk
ADD . /bsk

run ln -s /apps/john/run/john-local.conf lab_02/john-local.conf

RUN apt-get install -y python3-pip
RUN pip3 install -U setuptools
RUN pip3 install -U jupyter
RUN pip3 install -U RISE
RUN pip3 install -U cryptography
RUN jupyter-nbextension install rise --py --sys-prefix
RUN jupyter-nbextension enable rise --py --sys-prefix

EXPOSE 8888

CMD ["jupyter", "notebook", "--allow-root", "--no-browser", "--NotebookApp.token=''", "--ip", "0.0.0.0"]


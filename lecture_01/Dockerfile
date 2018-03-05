FROM linuxmintd/mint19-amd64

WORKDIR /bsk
ADD . /bsk

RUN apt-get install -y python3-pip
RUN pip3 install -U setuptools
RUN pip3 install -U jupyter
RUN pip3 install -U RISE
RUN pip3 install -U cryptography
RUN jupyter-nbextension install rise --py --sys-prefix
RUN jupyter-nbextension enable rise --py --sys-prefix

EXPOSE 8888

CMD ["jupyter", "notebook", "--allow-root", "--no-browser", "--NotebookApp.token=''", "--ip", "0.0.0.0"]


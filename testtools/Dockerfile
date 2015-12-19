FROM jdeathe/centos-ssh

MAINTAINER Richard Sedlak <richard.sedlak@mac.com>

USER root

ENV AP /data/app
ENV PATH $PATH:$AP

RUN yum -y install gcc

ADD Makefile $AP/
ADD memkiller.c $AP/

WORKDIR $AP

RUN make clean all

CMD ["./memkiller"]


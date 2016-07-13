FROM ubuntu:16.04
MAINTAINER Jess Portnoy <jess@packman.io>
RUN apt-get update && apt-get -y install build-essential debhelper dh-make apt-file wget aptitude sudo ca-certificates && apt-file update

# install packman
RUN echo "deb http://repo.packdaddy.io/apt/debian packman main" >> /etc/apt/sources.list.d/packman.list
RUN wget -O - http://repo.packdaddy.io/apt/packman.gpg.key|apt-key add -
RUN aptitude update && aptitude -y install packman 

# install NodeJS
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - && aptitude install -y nodejs

# install jo
RUN apt-add-repository ppa:duggan/jo --yes
RUN aptitude update -q && aptitude install jo
# install Docker
#RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
#RUN echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" > /etc/apt/sources.list.d/docker.list
#RUN aptitude update && aptitude -y install lxc-docker

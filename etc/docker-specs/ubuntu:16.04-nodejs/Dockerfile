FROM ubuntu:16.04
MAINTAINER Jess Portnoy <jess@packman.io>
RUN apt-get update && apt-get -y install build-essential debhelper dh-make apt-file wget aptitude sudo && apt-file update
RUN echo "deb http://repo.packman.io:8080/apt/debian packman main" >> /etc/apt/sources.list.d/packman.list
RUN wget -O - http://repo.packman.io:8080/apt/packman.gpg.key|apt-key add -
RUN aptitude update && aptitude -y install packman 
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - && aptitude install -y nodejs

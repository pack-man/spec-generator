FROM debian:8
MAINTAINER Jess Portnoy <jess@packman.io>
RUN apt-get update && apt-get -y install build-essential debhelper dh-make apt-file wget aptitude sudo && apt-file update
RUN echo "deb http://repo.packdaddy.io/apt/debian packman main" >> /etc/apt/sources.list.d/packman.list
RUN wget -O - http://repo.packdaddy.io/apt/packman.gpg.key|apt-key add -
RUN aptitude update && aptitude -y install packman 

FROM centos:7
MAINTAINER Jess Portnoy <jess@packman.io>
RUN rpm -ihv http://repo.packman.io:8080/rpm/noarch/packman-release.rpm
RUN yum -y install packman
RUN rpm -ihv https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN rpm -ihv http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm

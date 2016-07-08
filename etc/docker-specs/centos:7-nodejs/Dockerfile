FROM centos:7
MAINTAINER Jess Portnoy <jess@packman.io>
RUN rpm -ihv https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN rpm -ihv http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm
RUN rpm -ihv http://repo.packman.io:8080/rpm/noarch/packman-release.rpm
RUN yum clean all && yum -y install packman
# Node JS install
RUN curl --silent --location https://rpm.nodesource.com/setup_4.x | bash - && yum -y install nodejs
# Edit sudoers file 
# To avoid error: sudo: sorry, you must have a tty to run sudo 
RUN sed -i -e "s/Defaults    requiretty.*/ #Defaults    requiretty/g" /etc/sudoers

FROM centos:6
MAINTAINER Jess Portnoy <jess@packman.io>
# Edit sudoers file 
# To avoid error: sudo: sorry, you must have a tty to run sudo 
RUN sed -i -e "s/Defaults    requiretty.*/ #Defaults    requiretty/g" /etc/sudoers
RUN rpm -ihv http://repo.packman.io:8080/rpm/noarch/packman-release.rpm
RUN yum clean all && yum -y install packman
RUN rpm -ihv https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
RUN rpm -ihv http://packages.sw.be/rpmforge-release/rpmforge-release-0.5.2-2.el6.rf.x86_64.rpm

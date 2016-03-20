%define packman_home /home/packman
Name: packman
Version: 1.0.0
Release: 1
Summary: An End-to-End Software Packaging Platform.
BuildArch: noarch

#Group: @@PACKAGE_GROUP@@
License: AGPLv3+
URL: https://github.com/Packman/spec-generator
Packager: Jess Portnoy <jess@packman.com>


Source0: %{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires: @@BUILD_REQUIRES@@
Requires: rpm-build vim-enhanced wget unzip git sudo redhat-lsb-core

%description
An End-to-End Software Packaging Platform.
The Packman platform intends to relief the development team from the requirement of having packaging expertise by automating most of the work and providing guided package generation wizards when manual intervention is necessary.

Once package specifications have been defined, the platform will build the packages on all target platforms, run sanity [acceptance] tests and distribute the packages to a repository dedicated for the project.

This allows development teams to focus on what they do best: write software; and frees them from manual labour on packaging and distribution.

%prep
%setup -q

#%build


rm -rf %{buildroot}
@PACKMAN_HOME=/home/packman
mkdir -p $RPM_BUILD_ROOT$@PACKMAN_HOME/rpmbuild
for DIR in BUILD BUILDROOT RPMS SRPMS SOURCES;do
        mkdir ${RPM_BUILD_ROOT}${@PACKMAN_HOME}/rpmbuild/$DIR
done
mkdir -p ${RPM_BUILD_ROOT}%{packman_home}/tmp
cp -rp etc ${RPM_BUILD_ROOT}%{packman_home}/
cp -rp bin ${RPM_BUILD_ROOT}%{packman_home}/
mkdir -p ${RPM_BUILD_ROOT}%_defaultdocdir/%{name} ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}
cp -r README.md ${RPM_BUILD_ROOT}%_defaultdocdir/%{name}/
cp -r LICENSE ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}/

%clean
rm -rf %{buildroot}

%pre
getent group packman >/dev/null || groupadd -r packman  2>/dev/null
getent passwd packman >/dev/null || useradd -M -r -s /bin/bash -c "Packman user" -g packman packman 2>/dev/null


%post
if [ "$1" = 1 ];then
        cp /etc/sudoers /tmp/sudoers.new
        echo "## Done by Packman postinst" >> /tmp/sudoers.new
        echo "packman ALL=(ALL) NOPASSWD: /usr/bin/docker" >> /tmp/sudoers.new

        visudo -c -f /tmp/sudoers.new
        if [ $? -eq 0 ]; then
            cp /tmp/sudoers.new /etc/sudoers
        fi
        rm /tmp/sudoers.new
fi

%preun

%postun


%files
%defattr(-,packman,packman,-)
%doc %_defaultlicensedir/%{name}/* 
%doc %_defaultdocdir/%{name}/*
%dir %{packman_home}/bin
%dir %{packman_home}/etc
%dir %{packman_home}/tmp
%{packman_home}/*
%config %{packman_home}/etc/packman.rc
%config %{packman_home}/etc/packman-packages-meta/*
%config %{packman_home}/etc/docker-specs/*

%changelog
* Sat Mar 12 2016 Jess Portnoy <jess@packman.com> - 1.0.0-1
- First Packman RPM spec.


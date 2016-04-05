%global daemon_user @@DAEMON_USER@@
%global daemon_group @@DAEMON_GROUP@@

Name: @@PACKAGE_NAME@@
Version: @@PACKAGE_VERSION@@
Release: 1
Summary: @@PACKAGE_SUMMARY@@

License: @@PACKAGE_LICENSE@@
URL: @@PROJECT_URL@@
Packager: @@MAINTAINER_NAME@@ <@@MAINTAINER_EMAIL@@>


Source0: %{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires: @@BUILD_REQUIRES@@
#Requires: @@PACKAGE_REQUIRES@@

#Initscripts
Requires(post): chkconfig
Requires(preun): chkconfig initscripts

# Users and groups
Requires(pre): shadow-utils


%description
@@PACKAGE_DESCRIPTION@@


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}
#inspect the Makefile and see if there is a test target, if so then:
#make test


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%_defaultdocdir/%{name} ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}
# place license and README files in the right place.
mkdir -p ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}
if [ -r LICENSE ];then
	cp LICENSE ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}/
fi

for F in AUTHORS ChangeLog COPYING NEWS INSTALL README*;do
        if [ -r $F ];then
                cp $F ${RPM_BUILD_ROOT}%_defaultdocdir/%{name}/
        fi
done


%clean
rm -rf %{buildroot}

%pre
getent group %{daemon_group} >/dev/null || groupadd -r %{daemon_group}
getent passwd %{daemon_user} >/dev/null || \
useradd -r -g %{daemon_group} -d %{daemon_home} -s /bin/bash \
-c "%{name} user" %{daemon_user}

%post
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add %{name}
fi

%preun
if [ $1 -eq 0 ]; then
	/sbin/service %{name} stop >/dev/null 2>&1
	/sbin/chkconfig --del %{name}
fi


%postun


%files
%defattr(-,root,root,-)
%doc
%_defaultlicensedir/%{name}
%doc %_defaultdocdir/%{name}/*



%changelog


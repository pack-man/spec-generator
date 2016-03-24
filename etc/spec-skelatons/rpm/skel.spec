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

%description
@@PACKAGE_DESCRIPTION@@

%prep
%setup -q

%build
%configure
./configure --program-prefix= --disable-dependency-tracking --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin --sysconfdir=/etc --datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib64 --libexecdir=/usr/libexec --localstatedir=/var --sharedstatedir=/var/lib --mandir=/usr/share/man --infodir=/usr/share/info
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%_defaultdocdir/%{name} ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}
# place license and README files in the right place.
mkdir -p ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}
if [ -r LICENSE ];then
	cp LICENSE ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}/
fi
for R in README*;do
        cp README* ${RPM_BUILD_ROOT}%_defaultdocdir/%{name}/
done
for F in AUTHORS ChangeLog COPYING NEWS ;do
        if [ -r $F ];then
                cp $F ${RPM_BUILD_ROOT}%_defaultdocdir/%{name}/
        fi
done




%clean
rm -rf %{buildroot}

%pre

%post

%preun

%postun


%files
%defattr(-,root,root,-)
%doc
%_defaultlicensedir/%{name}
%doc %_defaultdocdir/%{name}/*


%changelog


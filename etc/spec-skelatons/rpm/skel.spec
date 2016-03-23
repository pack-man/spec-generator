Name: @@PACKAGE_NAME@@
Version: @@PACKAGE_VERSION@@
Release: 1
Summary: @@PACKAGE_SUMMARY@@

License: @@PACKAGE_LICENSE@@
URL: @@PROJECT_URL@@
Packager: @@MAINTAINER_NAME@@ <@@MAINTAINER_EMAIL@@>


Source0: %{name}-%{version}.tar.gz
BuildArch: @@BUILD_ARCH@@
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: @@BUILD_REQUIRES@@
Requires: @@PACKAGE_REQUIRES@@

%description
@@PACKAGE_DESCRIPTION@@

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%_defaultdocdir/%{name} ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}
# place license and README files in the right place.
cp -r README* ${RPM_BUILD_ROOT}%_defaultdocdir/%{name}/
cp -r LICENSE ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}/



%clean
rm -rf %{buildroot}

%pre

%post

%preun

%postun


%files
%defattr(-,root,root,-)
%doc
%_defaultlicensedir/%{name}/*
%doc %_defaultdocdir/%{name}/*


%changelog


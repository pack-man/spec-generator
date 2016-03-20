Name: packman-release
Version: 1.0.0
Release: 1
Summary: Packman repo release file and package configuration
BuildArch: noarch

#Group: @@PACKAGE_GROUP@@
License: AGPLv3+
URL: https://github.com/Packman/spec-generator
Packager: Jess Portnoy <jess@packman.com>
Source0: packman.repo

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
Packman repo release file. 
This package contains yum configuration for the Packman RPM Repository, as well as the public
GPG keys used to sign them.

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/packman.repo


%clean
rm -rf %{buildroot}


%preun

%postun


%files
%dir %{_sysconfdir}/yum.repos.d/
%config %{_sysconfdir}/yum.repos.d/packman.repo

%changelog
* Sat Mar 20 2016 Jess Portnoy <jess@packman.com> - 1.0.0-1
- First Packman repo file version.


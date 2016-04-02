# we'll embed these snippets in appropriate places in the spec if we have the need for a dev package

### dev package section
%package devel
Group: Development/Libraries
Summary: Development files for @@PACKAGE_NAME@@
#Requires: @@DEV_PACKAGE_REQUIRES@@ 

%description devel
Headers and additional dev files needed for building and developing on top of @@PACKAGE_NAME@@
### end dev package section

%files devel
%defattr(-,root,root)

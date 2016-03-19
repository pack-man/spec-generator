# What is Packman?
An End-to-End Software Packaging Platform.

The Packman platform intends to relief the development team from the need of having packaging expertise by automating most of the work and providing guided package generation wizards when manual intervention is necessary.

Once package specifications have been defined, the platform will build the packages on all target platforms, run sanity [acceptance] tests and distribute the packages to a repository dedicated for the project.

This allows development teams to focus on what they do best: write software; and frees them from manual labour on packaging and distribution.

## spec-generator
This module is the part of Packman that handles the initial package spec generation.
It consists of the following main stages:
-  A wizard that accepts inputs about the package meta data, i.e:
	- Package name
	- Package version
	- ENVs to build the package for
	- Source URL
	- Project home URL
	- Package description
	- Package maintainer
- Code to launch docker containers for each supported build ENV
- Code to analyse the project source code and generate a package spec [in the first phase RPM and deb formats will be supported but others will follow]


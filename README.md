# What is Packman?
An End-to-End Software Packaging Platform.

The Packman platform intends to relieve the development team from the need of having packaging expertise by automating most of the work and providing guided package generation wizards when manual intervention is necessary.

Once package specifications have been defined, the platform will build the packages on all target platforms, run sanity [acceptance] tests and distribute the packages to a repository dedicated for the project.

This allows development teams to focus on what they do best: write software; and frees them from manual labour on packaging and distribution.

## What Packaging formats does Packman support?
Packman is work in progress in very early stages.
It already produces RPM specs and calculates deps for C/C++ projects.

The plan for phase I is to fully support generation of RPM and deb packages for a variety of programming languages.

Later on, Packman will support additional packaging formats including Slackware tgz, FreeBSD pkgs and even Mac DMG packages.

## General Flow
- Get metadata input about the package to build
- Create a git repo for the package or use an existing one
- Launch Docker containers
- Analyse the project's source code and:
	- correct file permissions
	- lint all files to ensure valid syntax
	- determine needed build and runtime deps
	- generate pre and post install scripts
- Generate a package spec based on the target ENV [RPM for RHEL/CentOS/Suse, etc, deb for Debian/Ubuntu, etc]
- Build the package and test installation 
- Commit end result to repo

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

## scripts

- bin/packman-new-package: a wizard that generates an RC file describing the package metadata.
- bin/packman-prepare-build-env: downloads the source, fixes file permissions, runs dos2unix, generates a configure script if needed and re-packages the source for building
- bin/packman-gen-spec: uses the metadata collected from the user to generate a spec file, then builds the package and automatically calculates the package build and run time deps. 
- bin/packman-start-dockers: creates Docker containers per ENV, sets up SSH keys to push to the git repo and installs all needed packages for building, including Packman itself
- bin/packman-rpmchange: utility script for adding to the %changelog section
- bin/packman-functions.rc: functions used by the various Packman scripts

## config files
- etc/docker-specs: Docker files per supported disto
- etc/packman-packages-meta: Packman RC file skeleton and Packman package specs
- etc/spec-skelatons: Package spec skeletons for generating packages
- etc/packman.rc: Packman ENV settings
- etc/.bash\* - Packman BASH profile and RC 

## Setup instructions
### Installing the Packman RPM:
```
# rpm -ihv http://repo.packman.io:8080/rpm/noarch/packman-release.rpm
# yum install packman
```
### Installing the Packman deb:
```
# echo "deb http://repo.packman.io:8080/apt/debian packman main" >> /etc/apt/sources.list.d/packman.list
# wget -O - http://repo.packman.io:8080/apt/packman.gpg.key|apt-key add -
# aptitude install packman
```

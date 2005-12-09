Summary: The RAR Archiver
%define name rar
%define version 3.5.1
%define release 7dmay
Name: %{name}
Version: %{version}
Release: %{release}
License: Shareware
Group: Applications/Archiving
Source: %{name}-%{version}.tar.gz
Packager: Darrell May
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: i386
BuildRequires: e-smith-base
Requires: smeserver-release => 7.0

%description
RAR is a powerful tool which allows you to manage and control archive
files. The archive is usually a regular file, which name has a ".rar"
suffix.
 
%changelog
* Fri Dec 02 2005  Darrell May <dmay@myezserver.com>
- rar rebuild for SME 7.x
- [3.5.1-7dmay]

%prep

%setup

%build

%install
/bin/rm -rf $RPM_BUILD_ROOT

(cd root   ; /usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)
/bin/rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
%files -f %{name}-%{version}-filelist

%defattr(-,root,root)

%clean
/bin/rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

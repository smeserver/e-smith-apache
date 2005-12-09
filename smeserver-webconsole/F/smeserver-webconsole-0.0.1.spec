Summary: MindtermSSH for SME Server
%define name smeserver-webconsole
Name: %{name}
%define version 0.0.1
%define release 6
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Mitel/addon
Source: %{name}-%{version}.tar.gz
Packager: Darrell May <dmay@myezserver.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base
AutoReqProv: no
Obsoletes: dmc-mitel-webconsole
%description
%name is an implementation of http://www.appgate.com/mindterm on SME Server.
Access via https://yourdomain.com/webconsole.

%changelog
* Wed May 18 2005 Darrell May <dmay@myezserver.com>
- upgraded to MindTerm 2.4.2
- added support for SME 7.x
- [0.0.1-6]
* Sat Oct 12 2002 Darrell May <dmay@netsourced.com>
- upgraded to MindTerm 2.3.1
- [0.0.1-5]
* Fri Oct 11 2002 Darrell May <dmay@netsourced.com>
- upgraded to MindTerm 2.3
- [0.0.1-4]
* Tue Mar 03 2002 Darrell May <dmay@netsourced.com>
- changed rights/ownership for security
- [0.0.1-3]
* Tue Mar 03 2002 Darrell May <dmay@netsourced.com>
- changed %post/%postun to graceful
- [0.0.1-2]
* Sun Sep 23 2001 Darrell May <dmay@netsourced.com>
- name change
* Fri May 25 2001 Darrell May <dmay@netsourced.com>
- 0.0.1-1
- Original version

%prep

%setup

%build

%install
/bin/rm -rf $RPM_BUILD_ROOT
(cd root   ; /usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)
/bin/rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist \
$RPM_BUILD_ROOT \
| /bin/sed \
-e '/^.opt.administration.webconsole.*/s:^:%attr(0644,root,root):' \
> %{name}-%{version}-filelist

%clean
/bin/rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist

%defattr(-,root,root)

%pre

%post
/sbin/e-smith/db accounts set webconsole reserved
/sbin/e-smith/expand-template /etc/httpd/conf/httpd.conf
/etc/rc.d/init.d/httpd-e-smith restart

%preun

%postun
/sbin/e-smith/db accounts delete webconsole
/sbin/e-smith/expand-template /etc/httpd/conf/httpd.conf
/etc/rc.d/init.d/httpd-e-smith restart
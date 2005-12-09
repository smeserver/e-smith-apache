Summary: Backup to workstation panel for SME Server
%define name smeserver-backup2ws
Name: %{name}
%define version 0.0.1
%define release 31dmay
Version: %{version}
Release: %{release}
Copyright: GPL.
Group: Mitel/addon
Source: %{name}-%{version}.tar.gz
Packager: Darrell May
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
BuildRequires: e-smith-base
Requires: rar => 3.5.1 e-smith-release
Obsoletes: dmc-mitel-backup2ws

%description
%name provides a panel for performing server backups to Windows workstation share(s) using 
Rar (http://rarlabs.com) which is a robust shareware backup tool. It archives to either a single file
or may split archives over several files. It includes compression and provides proper saving and 
restoration of links and extended ownership/rights attributes. The files are viewable on the 
Windows workstation with WinRar.

%changelog
* Fri Dec 09 2005 Darrell May <dmay@myezserver.com>
- full restore now performed via *.* entry
- panel restore variables now support -\_\*
- restores now performed by listfile in backup2ws-restore action
- [0.0.1-31]
* Thu Dec 08 2005 Darrell May <dmay@myezserver.com>
- added -- stop switch scanning to rar command line in backup2ws-backup/restore actions
- volume size changed to megabytes (MB), panel updated
- cosmetic backup panel text changes
- panel restore variables now support -\_
- backups now performed by listfile in backup2ws-backup action
- [0.0.1-30]
* Wed Nov 30 2005 Darrell May <dmay@myezserver.com>
- removed rar & e-smith/sme specific version requirements
- requires rar installed/linked as /usr/bin/rar.
- config stored in SME 7.x format of /home/e-smith/db/backup2ws
- [0.0.1-29]
* Wed Nov 30 2005 Darrell May <dmay@myezserver.com>
- enhanced e-mailed report to include more detail
- [0.0.1-28]
* Thu Nov 24 2005 Darrell May <dmay@myezserver.com>
- removed rsync support
- added user definable Expiry time
- updated panel text
- [0.0.1-27]
* Wed Oct 26 2005 Darrell May <dmay@myezserver.com>
- added $BackupJob ARGV to {pre,post}-backup2ws-custom events called in ~actions/backup2ws-backup.
- [0.0.1-26]
* Wed Oct 26 2005 Darrell May <dmay@myezserver.com>
- added blank {pre,post}-backup2ws-custom events for advanced user usage.
- [0.0.1-25]
* Mon Oct 03 2005 Darrell May <dmay@myezserver.com>
- bug fix to ~actions/backup2ws-configure to set cron.d file modes 0644.
- [0.0.1-24]
* Mon Oct 03 2005 Darrell May <dmay@myezserver.com>
- update for SME 7.x
- [0.0.1-23]
* Tue May 03 2005 Darrell May <dmay@myezserver.com>
- bug fix to backup2ws-backup to correct 911 e-mail report
- [0.0.1-22]
* Mon Apr 11 2005 Darrell May <dmay@myezserver.com>
- added Compression option selector to panel
- bug fix to correctly delete same day backups
- [0.0.1-21]
* Mon Jan 24 2005 Darrell May <dmay@myezserver.com>
- fixed /sbin/e-smith/backup2ws-backup to delete mysql dumped tables at 911 completion
- [0.0.1-20]
* Mon Nov 22 2004 Darrell May <dmay@myezserver.com>
- fixed incorrect /dev/nul references to /dev/null
- [0.0.1-19]
* Sat Jan 17 2004 Darrell May <dmay@myezserver.com>
- bug fix to backup2ws-restore FULL restore
- [0.0.1-18]
* Thu Jan 08 2004 Darrell May <dmay@myezserver.com>
- rebuilt for SME Server 6.x support
- name change to smeserver
- [0.0.1-17]
* Thu Mar 13 2003 Darrell May <dmay@myezserver.com>
- refined 5.6 support for database backup, backup2ws-backup edited
- [0.0.1-16]
* Tue Mar 04 2003 Stephen Noble <stephen@dungog.net>
- added 5.6 support for database backup, backup2ws-backup edited
- [0.0.1-15]
* Wed Jan 08 2003 Darrell May <dmay@myezserver.com>
- added mySQL db backup to Disaster Recovery
- added Advanced Disaster Recovery restore post-upgrade event panel
- [0.0.1-14]
* Wed Jan 08 2003 Darrell May <dmay@myezserver.com>
- added Disaster Recovery option
- added full restore option
- [0.0.1-13]
* Tue Jan 07 2003 Darrell May <dmay@myezserver.com>
- added individual backup2ws job scheduling
- [0.0.1-12]
* Mon Jan 06 2003 Darrell May <dmay@myezserver.com>
- updated all /sbin/e-smith/backup2ws scripts
- [0.0.1-11]
* Sat Jan 04 2003 Darrell May <dmay@myezserver.com>
- added support for retaining rar backups for n days.
- [0.0.1-10]
* Thu Jan 02 2003 Darrell May <dmay@myezserver.com>
- updated /sbin/e-smith/backup2ws-restore
- [0.0.1-9]
* Thu Jan 02 2003 Darrell May <dmay@myezserver.com>
- updated all /sbin/e-smith/backup2ws scripts and panel
- [0.0.1-8]
* Thu Jan 02 2003 Darrell May <dmay@myezserver.com>
- updated all /sbin/e-smith/backup2ws scripts
- [0.0.1-7]
* Thu Jan 02 2003 Darrell May <dmay@myezserver.com>
- replaced dar with rar
- rebuilt all panels/functions for rar support
- [0.0.1-6]
* Mon Dec 30 2002 Darrell May <dmay@myezserver.com>
- [0.0.1-5]
- added logfiles and e-mail reporting
* Sun Dec 29 2002 Darrell May <dmay@myezserver.com>
- [0.0.1-4]
- added support for immediate backup
* Sun Dec 29 2002 Darrell May <dmay@myezserver.com>
- [0.0.1-3]
- added support for Disk ARchive
* Fri Dec 27 2002 Darrell May <dmay@myezserver.com>
- [0.0.1-2]
- minor enhancements
* Fri Dec 27 2002 Darrell May <dmay@myezserver.com>
- [0.0.1-1]
- Original version

%prep

%setup

%build
/usr/bin/perl createlinks

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
/etc/e-smith/events/actions/navigation-conf > /dev/null 2>&1
/sbin/e-smith/signal-event backup2ws-update

%preun

%postun

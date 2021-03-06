# $Id: e-smith-apache.spec,v 1.11 2010/03/04 16:31:07 slords Exp $

Summary: e-smith server and gateway - apache module
%define name e-smith-apache
Name: %{name}
%define version 2.2.0
%define release 6
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-apache-2.2.0-AddOffice2007MIMETypes.patch
Patch1: e-smith-apache-2.2.0-AddOpenOfficeMIMETypes.patch
Patch2: e-smith-apache-2.2.0-AddXMLMIMEType.patch
Patch3: e-smith-apache-2.2.0-AddOpenOffice2MIMETypes.patch
Patch4: e-smith-apache-2.2.0-optionDisableSSLv2.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base >= 4.15.1
Requires: e-smith-lib >= 1.15.1-19
Requires: e-smith-daemontools >= 1.7.1-01
Obsoletes: e-smith-proxypass
Obsoletes: e-smith-apache-proxy
Conflicts: e-smith-ibays < 1.0.2
AutoReqProv: no
BuildRequires: e-smith-devtools >= 1.11.0-12

%description
e-smith server and gateway software - apache module.

%changelog
* Sun Apr 26 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-6.sme
- Add option to disable SSLv2 [SME: 5034]

* Sat Mar 28 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-5.sme
- Add OpenOffice2 MIME Types [SME: 5112]

* Sat Mar  7 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-4.sme
- Add OpenOffice MIME Types [SME: 4848]
- Add XML MIME Type [SME: 5035]

* Thu Dec 11 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-3.sme
- Fix issues in patch that adds Microsoft Office 2007 MIME types [SME: 4548]

* Tue Dec 2 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-2.sme
- Add Microsoft Office 2007 MIME types [SME: 4548]

* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 2.2.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Tue Oct 23 2007 Filippo Carletti <filippo.carletti@gmail.com> 1.2.0-16
- Add SSL support to ProxyPass. [SME: 3481]

* Tue Sep 11 2007 Gavin Weight <gweight@gmail.com> 1.2.0-15
- Create/Move httpd logrotate.d directory. [SME: 3380]

* Tue Sep 11 2007 Gavin Weight <gweight@gmail.com> 1.2.0-14
- Rename apache to httpd in templates2expand. [SME: 3380]

* Wed Jun 6 2007 Shad L. Lords <slords@mail.com> 1.2.0-13
- Fix patch to exclude hosts if domains exist [SME: 2307]

* Fri May 18 2007 Shad L. Lords <slords@mail.com> 1.2.0-12
- Use correct lib for modules

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Fri Feb 23 2007 Shad L. Lords <slords@mail.com> 1.2.0-11
- Fix patch so template expands [SME: 2307]

* Fri Feb 23 2007 Shad L. Lords <slords@mail.com> 1.2.0-10
- Don't include host if domain exists [SME: 2307]

* Tue Feb 13 2007 Charlie Brady <charlie_brady@mitel.com> 1.2.0-9
- Gracefully handle differences in module names between apache
  versions. [SME: 2471]
- Add logrotate changes which should have been in 1.2.0-7 (patch
  was provided but not applied).

* Sat Jan 27 2007 Shad L. Lords <slords@mail.com> 1.2.0-8
- Remove proxypass fragment (now in e-smith-manager)

* Sat Jan 27 2007 Shad L. Lords <slords@mail.com> 1.2.0-8
- Remove proxypass fragment (now in e-smith-manager)

* Fri Jan 19 2007 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-7
- Move logrotate fragments from e-smith-base.

* Thu Dec 21 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-6
- Add support for optional modSSL{CertificateChainFile} [SME: 1779]

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Wed Nov 29 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-04
- Revert last change [SME: 2109]
- TODO: Split dev stream for that change
- Add Conflicts for latest e-smith-manager dev stream

* Wed Nov 08 2006 Charlie Brady <charlie_brady@mitel.com> 1.2.0-03
- Remove manager proxy pass fragment - moved to e-smith-manager.

* Sat Jul 15 2006 Charlie Brady <charlie_brady@mitel.com> 1.2.0-02
- Add ProxyPassReverse directives to allow redirects to work for proxy-
  passed virtual domains. Also proxy pass https to https. [SME: 1735]

* Tue Mar 14 2006 Charlie Brady <charlie_brady@mitel.com> 1.2.0-01
- Roll stable stream version. [SME: 1016]

* Mon Mar 13 2006 Charlie Brady <charlie_brady@mitel.com> 1.1.2-37
- Fix lookup of 'httpd' props in a few templates. Service name is
  httpd-e-smith. [SME: 1029]

* Fri Feb 10 2006 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-36
- Deny access to files starting with .ht typically
  .htaccess and .htpasswd [SME: 716]

* Tue Jan 31 2006 Gavin Weight <gweight@gmail.com> 1.1.2-35
- Change modPerl from enabled to disabled [SME: 575]

* Fri Jan 6 2006 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-34
- Add SVG filetype [SME: 374]

* Thu Dec 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-33
- And relocate the modSSL{CipherSuite} default to e-smith-base with
  the other modSSL defaults [SME: 194]

* Thu Dec 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-32
- Change default CipherSuite [SME: 194]
  Was: ALL:!ADH:RC4+RSA:+HIGH:+MEDIUM:-LOW:+SSLv2:-EXP
  Is: ALL:!aNULL:!ADH:!eNULL:!LOW:!EXP:RC4+RSA:+HIGH:+MEDIUM

* Thu Dec 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-31
- Moved SSL CipherSuite into db default - modSSL{CipherSuite} [SME: 194]

* Thu Dec 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-30
- Remove inode from FileETag response [SME: 198]

* Wed Dec 14 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-29
- Use literal HERE document to ensure braces in TRACE/TRACK rewrite [SME: 196]

* Wed Dec 14 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-28
- Add type for XSL stylesheet (.xsl) files [SME: 76]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-27
- Bump release number only

* Wed Aug 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-26]
- Add content from e-smith-apache-proxy, to enable apache to
  also operate as a non-caching proxy server. Add Obsoletes:
  header to ensure e-smith-apache-proxy RPM is removed on
  upgrade.

* Tue Aug  9 2005 Shad Lords <slords@mail.com>
- [1.1.2-25]
- Add directive for icons directory
- Fix newlines left on end of icons template
- Update server aliases to reference all local hosts [SF: 1246172]

* Wed Aug  3 2005 Shad Lords <slords@mail.com>
- [1.1.2-24]
- Fix Rewrite rule to include trailing stuff

* Wed Aug  3 2005 Shad Lords <slords@mail.com>
- [1.1.2-23]
- Update ProxyPass to use httpd-admin{TCPPort} [SF: 1246986]

* Wed Jul 27 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-22]
- Disable HTTP TRACK and TRACE in each VirtualDomain (patch by Gordon
  Rowell, with some further work by Shad Lords). [SF: 1240658]

* Wed Jul 27 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.2-21]
- Disable all low grade ciphers for SSL. [SF: 1240654]

* Tue Jul 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-20]
- Don't load userdir module by default. It's not used, and causes
  Nessus to complain. [SF: 1240657]

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-19]
- Patch from Shad: update rewrite and ProxyPass stuff for manager URLs.
  [SF: 1172203]

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-18]
- Add GPL COPYING file.

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-17]
- Clean up apache templates to use current DB interfaces.
- Make sure the single host ValidFrom specs for proxypass doesn't
  upset apache.

* Tue Jun 21 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-16]
- Make sure that DocumentRoot directory exists - latest apache2
  will not start up if not.

* Fri Jun 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-15]
- Do graceful restart of apache in domain-*, in case domain->ibay
  assignments have changed. [SF: 1222433]

* Wed Jun  8 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-14]
- Add rewrite fragment for httpd.conf to disable TRACE and TRACK
  requests.

* Fri May 27 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-13]
- Add support for TemplatePath => ProxyPassVirtualHost entries
  in domains db.

* Fri May 27 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-12]
- Bring ProxyPass fragment up to latest e-smith-lib APIs.

* Fri May 27 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-11]
- Remove ProxyPass support for various deprecated URIs. [SF: 1172203]
- Add content of e-smith-proxypass RPM. Add Obsoletes: header.

* Wed Mar 30 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-10]
- Add default TCPPort property to httpd-e-smith, so that correct
  hole is punched in firewall.

* Mon Mar 21 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-09]
- Remove mangling of syslog and apache log filenames - just
  retargeting the symlinks has the same effect. [MN00064132]

* Sun Mar 20 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-08]
- Remove logrotate-httpd which is obsoleted by generic_template_expand.

* Wed Mar 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-07]
- Fix dangling symlink in ibay-create. [MN00065576]

* Mon Mar 14 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-06]
- Use generic_template_expand action where possible, in place
  of specific actions. Update e-smith-lib dependency. [MN00064130]
- Replace all restart-* and most reload-* actions with calls to 'adjust-services'.
  Update e-smith-lib version dependency. [MN00065576]

* Tue Feb 22 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-05]
- Don't attempt to configure httpd.conf in post-install and post-upgrade.
  [MN00065717]

* Tue Jan 25 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-04]
- Remove stray ServiceLink sylinks. [MN00064757]

* Tue Dec 28 2004 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-03]
- Add "chpst -P" to httpd-e-smith run script, to protect runsv/supervise
  from term signals (wrongly) relayed by apache.  [charlieb MN00051144]

* Fri Dec 24 2004 Charlie Brady <charlieb@e-smith.com>
- [1.1.2-02]
- Remove  ValidFrom defaults fragment for httpd-admin - as it duplicates
  one in e-smith-base. [MN00062533]

* Wed Nov 17 2004 Mark Knox <markk@e-smith.com>
- [1.1.2-01]
- Picking up new directory. MN00056429.

* Wed Nov 17 2004 Mark Knox <markk@e-smith.com>
- [1.1.1-03]
- Added empty ValidFrom defaults fragment [markk MN00056429]

* Tue Nov  9 2004 Charlie Brady <charlieb@e-smith.com>
- [1.1.1-02]
- Modify config and run script for compatibility with apache 2. Most of these
  changes were contributed by Shad Lords. [charlieb MN00051144]

* Mon Oct  4 2004 Charlie Brady <charlieb@e-smith.com>
- [1.1.1-01]
- New development stream for apache 2 - 1.1.1

* Fri Sep  3 2004 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-23]
- Clean BuildRequires. [charlieb MN00043055]

* Tue Jul 13 2004 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-22]
- Updated modPerl templates to remove use of esmith::config.
  [msoulier MN00039579]

* Tue Jun 22 2004 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-21]
- Added RewriteCond statements to previous RewriteRules to exclude localhost,
  so ssh port-forwarding is not broken. [msoulier MN00020885]

* Fri Jun 18 2004 Tony Clayton <apc@e-smith.com>
- [1.1.0-20]
- Fix LoadModule fragment from last patch [tonyc 11348]

* Mon Jun 14 2004 Tony Clayton <apc@e-smith.com>
- [1.1.0-19]
- Add modPerl service and httpd.conf templates [tonyc 11348]

* Mon May 10 2004 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-18]
- Adding rewrite rules to prevent plaintext access to the server manager.
  [msoulier MN00020885]

* Thu May  6 2004 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-17]
- Added httpd-admin's remoteaccess list to permissible networks for
  server-resources. [msoulier MN00024949]

* Mon Feb 23 2004 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-16]
- Backing-out last change. [msoulier dpar-21489]

* Mon Feb 23 2004 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-15]
- Added restart-httpd-graceful to domain-* events. [msoulier dpar-21489]

* Wed Feb 18 2004 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-14]
- Updating requires to e-smith-daemontools. [msoulier 7629]

* Wed Feb 18 2004 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-13]
- Updating restart-httpd-graceful to use new daemontools sigusr1 option.
  [msoulier 7629]

* Wed Jan 21 2004 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-12]
- Staggering the symlinks a little farther. [msoulier 9955]

* Wed Jan 21 2004 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-11]
- Adding symlinks to the service-domain-create event for httpd restart.
  [msoulier 9955]

* Tue Dec  9 2003 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-10]
- Fixed another error in the specfile, resulting in incorrect file
  permissions. [msoulier 7629]
- Updated action scripts for supervise. [msoulier 7629]

* Tue Dec  9 2003 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-09]
- Fixed an error in the specfile. [msoulier 7629]

* Tue Dec  9 2003 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-08]
- Updated createlinks for daemontools. [msoulier 7629]

* Tue Dec  9 2003 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-07]
- Putting httpd-e-smith under supervision. [msoulier 7629]

* Thu Sep 18 2003 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-06]
- Added a null-string return value to the end of 00Setup, ensure no output
  from that fragment. [msoulier 9803]

* Wed Sep  3 2003 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-05]
- Use implementation class, not virtual class in  VirtualHosts/00Setup fragment.
  [charlieb 9803]

* Wed Sep  3 2003 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-04]
- Added a 75AddType05.exe fragment to specify a proper mime-type for .exe
  files. [msoulier 9866]

* Fri Aug 29 2003 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-03]
- Allow TemplatePath property in domain record to specify an alternate template
  subdir for virtual host content specification (e.g. to proxypass a domain).
  [charlieb 8409]

* Fri Aug 29 2003 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-02]
- Changed the VirtualHosts subtemplate to pass the domain object instead of db handle,
  and modified VirtualHosts/00Setup fragment to convert it to the right class.
  Fix scoping problem with the blessed object. [charlieb 9803]

* Fri Aug 29 2003 Michael Soulier <msoulier@e-smith.com>
- [1.1.0-01]
- rolling to dev stream - 1.1.0

* Fri Aug 29 2003 Michael Soulier <msoulier@e-smith.com>
- [1.0.0-04]
- Added a 00Setup fragment to VirtualHosts to process the %domainsdb hash back
  into an esmith::DomainsDB object. [msoulier 9803]

* Mon Aug 25 2003 Michael Soulier <msoulier@e-smith.com>
- [1.0.0-03]
- Added a reference to the domains db in the extra data for processing the
  VirtualHosts fragments. [msoulier 9803]

* Fri Aug  1 2003 Michael Soulier <msoulier@e-smith.com>
- [1.0.0-02]
- Fixed a precedence error that broke virtual hosts in apache.
  [msoulier 9640]

* Wed Jul  9 2003 Charlie Brady <charlieb@e-smith.com>
- [1.0.0-01]
- Setting to release version number  - 1.0.0

* Wed Jul  9 2003 Michael Soulier <msoulier@e-smith.com>
- [0.2.0-04]
- Fixed breakage in admin web server when a local network with a 32-bit subnet
  mask is used. [msoulier 9259]

* Thu Jul  3 2003 Charlie Brady <charlieb@e-smith.com>
- [0.2.0-03]
- Fix log noise problem in expansion of httpd.conf template. [charlieb 9269]

* Wed Jul  2 2003 Charlie Brady <charlieb@e-smith.com>
- [0.2.0-02]
- List primary domain as first (default) virtual domain in apache config.
  Include $SystemName.domain.name in ServerAlias directive. [charlieb 9241]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [0.2.0-01]
- Changing version to stable stream number - 0.2.0

* Thu Jun 12 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.2-01]
- Add order to migrate fragments [gordonr 9015]

* Wed Jun 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.1-02]
- Fixed Conflicts header - should be <, not <= [gordonr 8903]

* Fri Jun  6 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.1-01]
- Shuffled some httpd.conf fragments to e-smith-ibays [gordonr 8903]

* Wed May 28 2003 Michael Soulier <msoulier@e-smith.com>
- [0.1.0-19]
- Moving httpd-e-smith init script to e-smith-apache. [msoulier 8852]

* Tue Apr 29 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.0-18]
- Do an explicit die if the httpd-e-smith record is missing from the
  config db, rather than an implicit die due to an invalid object
  reference [gordonr 8609]

* Wed Apr  9 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.0-17]
- Relocated conf-httpd from e-smith-base [gordonr 8150]

* Fri Apr  4 2003 Mark Knox <markk@e-smith.com>
- [0.1.0-16]
- Moved restart-httpd-* actions from base [markk 5509]

* Fri Apr  4 2003 Mark Knox <markk@e-smith.com>
- [0.1.0-15]
- Moved db config fragments here from e-smith-base [markk 5509]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.0-14]
- Make /server-resources/ browsable from LAN [gordonr 6620]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.0-13]
- Delete Apache ReadmeName directive [gordonr 6313]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.0-12]
- Fixed broken conf-httpd-e-smith links in post-{install,upgrade} [gordonr 7960]

* Tue Mar 18 2003 Lijie Deng <lijied@e-smith.com>
- [0.1.0-11]
- Deleted ./etc/httpd/conf/httpd.conf/template-begin 
  deleted ./etc/httpd/conf/srm.conf/template-begin
  deleted ./etc/httpd/conf/access.conf/template-begin [lijied 3295]

* Mon Mar 17 2003 Lijie Deng <lijied@e-smith.com>
- [0.1.0-10]
- Delete empty template-end file  [lijied 3295]
  
* Wed Mar 12 2003 Charlie Brady <charlieb@e-smith.com>
- [0.1.0-09]
- Remove more references to primary and wwwpublic in favour
  of the "Primary" i-bay. There is still some special case code,
  which might go later if it turns out not to be needed.
  [charlieb 5652]

* Tue Mar 11 2003 Mark Knox <markk@e-smith.com>
- [0.1.0-08]
- Fixed a missing quote in 27ManagerProxyPass [markk 7635]

* Tue Mar 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.0-07]
- Pass externalSSLAccess and localAccess to VirtualDomains fragments so they don't
  need to recalculate these values [gordonr 7635]
- Use early return from 27ManagerProxyPass and new DB interface [gordonr 7635]

* Mon Mar 10 2003 Charlie Brady <charlieb@e-smith.com>
- [0.1.0-06]
- Remove special case handling for /home/e-smith/files/primary in Apache
  configuration. Migrate code and db entries for wwwpublic to Public.
  [charlieb 5652]

* Fri Mar  7 2003 Charlie Brady <charlieb@e-smith.com>
- [0.1.0-05]
- Replace deprecated CONFREF with MORE_DATA in processTemplate call in
  VirtualHosts fragment of httpd.conf templates. Fixes template
  expansion breakage (I'm not sure what broke it, but this fixes it.)
  [charlieb]
- Add default config db fragments to set type and status. Remove redundant
  conf-httpd-e-smith script. [charlieb 1507]

* Fri Jan 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.0-04]
- Move SSL initialisation to global context [gordonr 1432]

* Fri Jan 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [0.1.0-03]
- Use default SSL certificate of $SystemName.$DomainName [gordonr 4874]

* Wed Jan  8 2003 Mark Knox <markk@e-smith.com>
- [0.1.0-02]
- Added conf-httpd-e-smith action linked to the same events as conf-startup
  in e-smith-base [markk 6428]

* Mon Jan 06 2003 Mark Knox <m_knox@mitel.com>
- [0.1.0-01]
- Initial release, split out from e-smith-base [markk 6428]

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%pre

%post

%build
perl createlinks
mkdir -p root/service
ln -s /var/service/httpd-e-smith root/service/httpd-e-smith
mkdir -p root/var/service/httpd-e-smith/supervise
touch root/var/service/httpd-e-smith/down

mkdir -p root/etc/httpd
mkdir -p root/var/state/httpd
ln -s ../../var/state/httpd root/etc/httpd/state

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --dir /var/service/httpd-e-smith 'attr(01755,root,root)' \
    --file /var/service/httpd-e-smith/down 'attr(0644,root,root)' \
    --file /var/service/httpd-e-smith/run 'attr(0755,root,root)' \
    > e-smith-%{version}-filelist

echo "%doc COPYING"          >> e-smith-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)

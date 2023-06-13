%global _missing_build_ids_terminate_build 0

# Package namespaces
%global ns_name ea
%global ns_dir /opt/cpanel
%global _scl_prefix %ns_dir

%scl_package %scl

# This makes the ea-php<ver>-build macro stuff work
#%scl_package_override

%global inifile 01-ioncube.ini

Name:    %{?scl_prefix}php-ioncube12
Vendor:  cPanel, Inc.
Summary: v12 Loader for ionCube-encoded PHP files
Version: 12.0.5
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4572 for more details
%define release_prefix 2
Release: %{release_prefix}%{?dist}.cpanel
License: Redistributable
Group:   Development/Languages
URL:     http://www.ioncube.com/loaders.php

# 1. See `perldoc find-latest-version` for info on the tarball.
# 2. The archive contains the license file, so no need to have it as a
#    separate source file.
Source: ioncube_loaders_lin_x86-64.tar.gz

BuildRequires: scl-utils-build
BuildRequires: %{?scl_prefix}scldevel
BuildRequires: %{?scl_prefix}build
BuildRequires: %{?scl_prefix}php-devel
Requires:      %{?scl_prefix}php(zend-abi) = %{php_zend_api}
Requires:      %{?scl_prefix}php(api) = %{php_core_api}
Requires:      %{?scl_prefix}php-cli
Provides:      %{?scl_prefix}ioncube = 12
Conflicts:     %{?scl_prefix}ioncube >= 12, %{?scl_prefix}ioncube < 12
Conflicts:     %{?scl_prefix}php-ioncube
Conflicts:     %{?scl_prefix}php-ioncube5
Conflicts:     %{?scl_prefix}php-ioncube6
Conflicts:     %{?scl_prefix}php-ioncube10
Conflicts:     %{?scl_prefix}php-ioncube11

# Don't provide extensions as shared library resources
%{?filter_provides_in: %filter_provides_in %{php_extdir}/.*\.so$}
%{?filter_setup}

%description
The v12 ionCube Loader enables use of ionCube-encoded PHP files running
under PHP %{php_version}.

%prep
%setup -q -n ioncube

%build
# Nothing to do here, since it's a binary distribution.

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf %{buildroot}

# The module itself
install -d -m 755 $RPM_BUILD_ROOT%{php_extdir}
install -m 755 ioncube_loader_lin_%{php_version}.so $RPM_BUILD_ROOT%{php_extdir}

# The ini snippet
install -d -m 755 $RPM_BUILD_ROOT%{php_inidir}
cat > $RPM_BUILD_ROOT%{php_inidir}/%{inifile} <<EOF
; Enable v12 IonCube Loader extension module
zend_extension="%{php_extdir}/ioncube_loader_lin_%{php_version}.so"
EOF

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.txt
%config(noreplace) %{php_inidir}/%{inifile}
%{php_extdir}/ioncube_loader_lin_%{php_version}.so

%changelog
* Tue Apr 04 2023 Julian Brown <julian.brown@cpanel.net> - 12.0.5-2
- ZC-10047: Do not build on Ubuntu 22

* Tue Dec 27 2022 Cory McIntire <cory@cpanel.net> - 12.0.5-1
- EA-11120: Update scl-ioncube12 from v12.0.4 to v12.0.5

* Mon Dec 12 2022 Cory McIntire <cory@cpanel.net> - 12.0.4-1
- EA-11094: Update scl-ioncube12 from v12.0.3 to v12.0.4

* Mon Dec 05 2022 Cory McIntire <cory@cpanel.net> - 12.0.3-1
- EA-11079: Update scl-ioncube12 from v12.0.2 to v12.0.3

* Mon Sep 12 2022 Cory McIntire <cory@cpanel.net> - 12.0.2-1
- EA-10932: Update scl-ioncube12 from v12.0.1 to v12.0.2

* Mon Aug 15 2022 Brian Mendoza <brian.mendoza@cpanel.net> - 12.0.1-2
- ZC-10213: Update find-latest-version script

* Fri Aug 12 2022 Brian Mendoza <brian.mendoza@cpanel.net> - 12.0.1-1
- ZC-10213: Create package


#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	3GPP AMR-NB Floating-point Speech Codec
Summary(pl.UTF-8):	Zmiennoprzecinkowy kodek mowy 3GPP AMR-NB
Name:		amrnb
Version:	6.1.0.4
Release:	1
# 26104-610.doc says:
# Copyright Notification
# No part may be reproduced except as authorized by written permission.
# The copyright and the foregoing restriction extend to reproduction in all media.
# (c) 2004, 3GPP Organizational Partners (ARIB, CCSA, ETSI, T1, TTA, TTC).
# All rights reserved.
License:	restricted
Group:		Libraries
Source0:	http://ftp.penguin.cz/pub/users/utx/amr/%{name}-%{version}.tar.bz2
# Source0-md5:	f482cdd0584469ba23ff33c6b331acbd
Source1:	http://www.3gpp.org/ftp/Specs/archive/26_series/26.104/26104-610.zip
# NoSource1-md5:	cfd9012bff83afdf5ad069b86d3063b6
NoSource:	1
URL:		http://www.3gpp.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
3GPP AMR-NB Floating-point Speech Codec.

%description -l pl.UTF-8
Zmiennoprzecinkowy kodek mowy 3GPP AMR-NB.

%package devel
Summary:	Header files for amrnb library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki amrnb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for amrnb library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki amrnb.

%package static
Summary:	Static amrnb library
Summary(pl.UTF-8):	Statyczna biblioteka amrnb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static amrnb library.

%description static -l pl.UTF-8
Statyczna biblioteka amrnb.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc 26104-610.doc readme.txt
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/amrnb-*
%attr(755,root,root) %{_libdir}/libamrnb.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libamrnb.so
%{_libdir}/libamrnb.la
%{_includedir}/amrnb

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libamrnb.a
%endif

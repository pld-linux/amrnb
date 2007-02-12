#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	3GPP AMR Floating-point Speech Codec
Summary(pl.UTF-8):   Zmiennoprzecinkowy kodek mowy 3GPP AMR
Name:		amrnb
Version:	0.0.1
Release:	2
# AUTHORS specifies "License unknown", 26104-610.doc in original sources says:
# Copyright Notification
# No part may be reproduced except as authorized by written permission.
# The copyright and the foregoing restriction extend to reproduction in all media.
# (c) 2004, 3GPP Organizational Partners (ARIB, CCSA, ETSI, T1, TTA, TTC).
# All rights reserved.
License:	restricted
Group:		Libraries
# autotooled version of http://www.3gpp.org/ftp/Specs/latest/Rel-6/26_series/26104-610.zip
Source0:	http://ronald.bitfreak.net/priv/%{name}-%{version}.tar.gz
# NoSource0-md5:	c4546d2920cf287847a7286b4dea7472
NoSource:	0
Patch0:		%{name}-inttypes.patch
URL:		http://www.3gpp.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%description
3GPP AMR Floating-point Speech Codec.

%description -l pl.UTF-8
Zmiennoprzecinkowy kodek mowy 3GPP AMR.

%package devel
Summary:	Header files for amrnb library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki amrnb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for amrnb library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki amrnb.

%package static
Summary:	Static amrnb library
Summary(pl.UTF-8):   Statyczna biblioteka amrnb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static amrnb library.

%description static -l pl.UTF-8
Statyczna biblioteka amrnb.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%doc AUTHORS README
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

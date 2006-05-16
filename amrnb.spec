#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	3GPP AMR Floating-point Speech Codec
Summary(pl):	Zmiennoprzecinkowy kodek mowy 3GPP AMR
Name:		amrnb
Version:	0.0.1
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://ronald.bitfreak.net/priv/%{name}-%{version}.tar.gz
# Source0-md5:	c4546d2920cf287847a7286b4dea7472
Patch0:		%{name}-inttypes.patch
URL:		http://www.3gpp.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%description
3GPP AMR Floating-point Speech Codec.

%description -l pl
Zmiennoprzecinkowy kodek mowy 3GPP AMR.

%package devel
Summary:	Header files for amrnb library
Summary(pl):	Pliki nag³ówkowe biblioteki amrnb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for amrnb library.

%description devel -l pl
Pliki nag³ówkowe biblioteki amrnb.

%package static
Summary:	Static amrnb library
Summary(pl):	Statyczna biblioteka amrnb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static amrnb library.

%description static -l pl
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

Summary:	Pixel Filter for colorblind accessibility
Name:		libcolorblind
Version:	0.0.1
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://ftp.debian.org/debian/pool/main/c/colorblind/colorblind_%{version}.orig.tar.gz
# Source0-md5:	c4b79e74f4e4edc02620e850cfcddd4e
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides an unified way to recalculate colors in order to
present alternative views on images for colorblind people.

%package devel
Summary:	Header files for libcolorblind library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcolorblind
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcolorblind library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcolorblind.

%package static
Summary:	Static libcolorblind library
Summary(pl.UTF-8):	Statyczna biblioteka libcolorblind
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcolorblind library.

%description static -l pl.UTF-8
Statyczna biblioteka libcolorblind.

%prep
%setup -q -n colorblind-%{version}.orig

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libcolorblind.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcolorblind.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcolorblind.so
%{_libdir}/libcolorblind.la
%{_includedir}/colorblind.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcolorblind.a

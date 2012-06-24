#
# Conditional build:
%bcond_without	static_libs	# without static version
#
Summary:	MSWord Document to HTML converter
Summary(pl):	Konwerter dokument�w MS Worda do HTML
Summary(pt_BR):	Conversor de arquivos formato Word (6/7/8/9) para html
Name:		wv
Version:	1.2.1
Release:	4
License:	GPL
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/wvware/%{name}-%{version}.tar.gz
# Source0-md5:	d757080af4595839d5d82a1a573c692c
Patch0:		%{name}-gsfinput.patch
URL:		http://wvware.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.12.2
BuildRequires:	libgsf-devel >= 1.14.1
BuildRequires:	libpng-devel >= 1.2.12
BuildRequires:	libtool
BuildRequires:	libwmf-devel >= 2:0.2.8.4
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
# these are required for full libwmf
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	libjpeg-devel
BuildRequires:	xorg-lib-libX11-devel
Obsoletes:	mswordview
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	 -fomit-frame-pointer 

%description
MSWordView is a program that understands the Microsoft Word 8 binary
file format (Office97, Office2000) and is able to convert Word
documents into HTML, which can then be read with a browser.

wv is a suite of programs to help convert Word Documents to HTML.

%description -l pl
MSWordView jest programem, kt�ry rozumie binarne dokumenty programu
Microsoft Word 8 (Office97, Office2000) i jest w stanie skonwertowa�
je do dokumentu HTML, kt�ry mo�e by� przeczytany w przegl�darce WWW.

wv jest elementem program�w, kt�re pomagaj� przekonwertowa� dokumenty
Worda do HTML.

%description -l pt_BR
Conversor de arquivos formato Word (6/7/8/9) para html.

%package devel
Summary:	Include files needed to compile
Summary(pl):	Pliki nag��wkowe do biblioteki wv
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.12.2
Requires:	libgsf-devel >= 1.14.1
Requires:	libpng-devel >= 1.2.12
Requires:	libwmf-devel >= 2:0.2.8.4
Requires:	libxml2-devel >= 1:2.6.26
# these are required for full libwmf
Requires:	freetype-devel >= 2.0
Requires:	libjpeg-devel
Requires:	xorg-lib-libX11-devel

%description devel
Contains the header files.

%description devel -l pl
Pakiet tem zawiera pliki nag��wkowe wv.

%package static
Summary:	Static wv libraries
Summary(pl):	Biblioteki statyczne wv
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com o wv
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Contains static wv libraries.

%description static -l pl
Pakiet zawiera statyczne biblioteki wv.

%prep
%setup -q
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-zlib \
	--with-png \
	--with-libwmf \
	--%{!?with_static_libs:dis}%{?with_static_libs:en}able-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/wv*
%attr(755,root,root) %{_libdir}/libwv-*.so.*.*.*
%{_datadir}/wv
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwv.so
%{_libdir}/libwv.la
%{_includedir}/wv
%{_pkgconfigdir}/wv-*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libwv.a
%endif

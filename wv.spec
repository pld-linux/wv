#
# Conditional build:
# _without_static	- without static version
#
Summary:	MSWord Document to HTML converter
Summary(pl):	Konwerter dokumentów MS Worda do HTML
Summary(pt_BR):	Conversor de arquivos formato Word (6/7/8/9) para html
Name:		wv
Version:	0.7.6
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/wvware/%{name}-%{version}.tar.gz
# Source0-md5:	28c46d6676e0fce6a19e3cb730b04556
Patch0:		%{name}-magick.patch
Patch1:		%{name}-fixes.patch
URL:		http://www.wvWare.com/
BuildRequires:	ImageMagick-devel >= 1:5.5.2.5
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-static
BuildRequires:	expat-devel
BuildRequires:	glib2-devel
BuildRequires:	libtool
BuildRequires:	libltdl-static
BuildRequires:	libwmf-devel >= 0.2.2
#BuildRequires:	libxml2-devel (may be used _instead of_ expat)
BuildRequires:	pkgconfig
Obsoletes:	mswordview
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MSWordView is a program that understands the Microsoft Word 8 binary
file format (Office97, Office2000) and is able to convert Word
documents into HTML, which can then be read with a browser.

wv is a suite of programs to help convert Word Documents to HTML.

%description -l pl
MSWordView jest programem, który rozumie binarne dokumenty programu
Microsoft Word 8 (Office97, Office2000) i jest w stanie skonwertowaæ
je do dokumentu HTML, który mo¿e byæ przeczytany w przegl±darce WWW.

wv jest elementem programów, które pomagaj± przekonwertowaæ dokumenty
Worda do HTML.

%description -l pt_BR
Conversor de arquivos formato Word (6/7/8/9) para html.

%package devel
Summary:	Include files needed to compile
Summary(pl):	Pliki nag³ówkowe do biblioteki wv
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Contains the header files.

%description devel -l pl
Pakiet tem zawiera pliki nag³ówkowe wv.

%package static
Summary:	Static wv libraries
Summary(pl):	Biblioteki statyczne wv
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com o wv
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Contains static wv libraries.

%description static -l pl
Pakiet zawiera statyczne biblioteki wv.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake} -i
%configure \
	--with-expat \
	--with-exporter \
	--with-glib=glib2 \
	--with-libwmf \
	--with-png \
	--with-zlib \
	--%{?_without_static:dis}%{!?_without_static:en}able-static \
	--with-libxml2
# possible bconds:
# --with-glib=glib2 to use glib 2.x instead of 1.x
# --with-gnomevfs to include gnomevfs support (gnome1 only?)

mv -f magick magick-wv
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir}

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%doc CHANGELOG CREDITS D_CREDITS D_README KNOWN-BUGS README TESTING TODO.TXT
%attr(755,root,root) %{_bindir}/wv*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/wv
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libwv-config
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%if %{!?_without_static:1}%{?_without_static:0}
%files static
%defattr(644,root,root,755)
%{_libdir}/libwv.a
%endif

Summary:	MSWord Document to HTML converter
Summary(pl):	Konwerter domumentów MSWord do HTML
Name:		wv
Version:	0.6.4
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Vendor:		Caolan McNamara <Caolan.McNamara@ul.ie>
Source0:	http://download.sourceforge.net/wvware/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.wvWare.com/
BuildRequires:	autoconf
BuildRequires:	ImageMagick-devel
BuildRequires:	freetype-devel
BuildRequires:	XFree86-devel
BuildRequires:	libwmf-devel >= 0.1.21b-3
BuildRequires:	gd-devel
BuildRequires:	glib-devel
BuildRequires:	iconv
Requires:	iconv
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

%package devel
Summary:	Include files needed to compile
Summary(pl):	Pliki nag³ówkowe do biblioteki 
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Contains the header files.

%description -l pl devel
Pakiet tem zawiera pliki nag³ówkowe.

%package static
Summary:	Static libraries
Summary(pl):	Biblioteki statyczne
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Contains static libraries.

%description -l pl static
Pakiet zawiera statyczne biblioteki.

%prep
%setup -q -n %{name}
%patch0 -p1

# Checking for CVS specific files and removing them.
find . -type d -name 'CVS'| xargs rm -rf

%build
for var in HAVE_TTF HAVE_WMF HAVE_XPM HAVE_ZLIB HasPNG MATCHED_TYPE \
	MUST_USE_INTERNAL_ICONV_TABLE USE_ICONV USE_X XML_BYTE_ORDER \
	HAVE_GLIB HAVE_LIBXML2 ; do
		echo "#undef $var" >> acconfig.h
done
autoheader
%configure \
	--with-exporter \
	--with-zlib \
	--with-png \
	--with-Magick \
	--with-xpm=/usr/X11R6

echo "#define SYSTEM_ZLIB" >> config.h

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf helper-scripts/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc helper-scripts
%attr(755,root,root) %{_bindir}/*
%{_datadir}/wv
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libwv.a

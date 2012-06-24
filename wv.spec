Summary:	MSWord Document to HTML converter
Summary(pl):	Konwerter domument�w MSWord do HTML
Name:		wv
Version:	0.6.5
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Vendor:		Caolan McNamara <Caolan.McNamara@ul.ie>
Source0:	http://download.sourceforge.net/wvware/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-magick.patch
URL:		http://www.wvWare.com/
BuildRequires:	XFree86-devel
BuildRequires:	ImageMagick-devel
BuildRequires:	autoconf
BuildRequires:	freetype1-devel
BuildRequires:	gd-devel
BuildRequires:	glib-devel
#BuildRequires:	libwmf-devel >= 0.1.21b-3
#BuildRequires:	libxml2-devel
BuildRequires:	autoconf
Obsoletes:	mswordview
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package devel
Summary:	Include files needed to compile
Summary(pl):	Pliki nag��wkowe do biblioteki wv
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Contains the header files.

%description -l pl devel
Pakiet tem zawiera pliki nag��wkowe wv.

%package static
Summary:	Static wv libraries
Summary(pl):	Biblioteki statyczne wv
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Contains static wv libraries.

%description -l pl static
Pakiet zawiera statyczne biblioteki wv.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# Checking for CVS specific files and removing them.
find . -type d -name 'CVS'| xargs rm -rf

%build
autoconf
%configure \
	--with-exporter \
	--with-zlib \
	--with-png \
	--with-Magick
#	--with-libwmf

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGELOG CREDITS D_CREDITS D_README KNOWN-BUGS README TESTING TODO.TXT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/wv
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libwv.a

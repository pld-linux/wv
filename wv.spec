Summary:	MSWord Document to HTML converter
Summary(es):	MSWord 6/7/8/9 binary file format -> HTML converter
Summary(pl):	Konwerter domumentÛw MSWord do HTML
Summary(pt_BR):	Conversor de arquivos formato Word (6/7/8/9) para html
Name:		wv
Version:	0.7.0
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
Patch2:		%{name}-ac_fix.patch
URL:		http://www.wvWare.com/
BuildRequires:	XFree86-devel
BuildRequires:	ImageMagick-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype1-devel
BuildRequires:	gd-devel >= 2.0.1
BuildRequires:	glib-devel
BuildRequires:	libtool
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
MSWordView jest programem, ktÛry rozumie binarne dokumenty programu
Microsoft Word 8 (Office97, Office2000) i jest w stanie skonwertowaÊ
je do dokumentu HTML, ktÛry moøe byÊ przeczytany w przegl±darce WWW.

wv jest elementem programÛw, ktÛre pomagaj± przekonwertowaÊ dokumenty
Worda do HTML.

%description -l pt_BR
Conversor de arquivos formato Word (6/7/8/9) para html

%package devel
Summary:	Include files needed to compile
Summary(pl):	Pliki nag≥Ûwkowe do biblioteki wv
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Contains the header files.

%description -l pl devel
Pakiet tem zawiera pliki nag≥Ûwkowe wv.

%package static
Summary:	Static wv libraries
Summary(pl):	Biblioteki statyczne wv
Summary(pt_BR):	Bibliotecas est·ticas para desenvolvimento com o wv
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Contains static wv libraries.

%description -l pl static
Pakiet zawiera statyczne biblioteki wv.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Checking for CVS specific files and removing them.
find . -type d -name 'CVS'| xargs rm -rf

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
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

Summary:	MSWord Document to HTML converter
Summary(es):	MSWord 6/7/8/9 binary file format -> HTML converter
Summary(pl):	Konwerter domumentÛw MSWord do HTML
Summary(pt_BR):	Conversor de arquivos formato Word (6/7/8/9) para html
Name:		wv
Version:	0.7.1
Release:	1
License:	GPL
Group:		Applications/Text
Group(cs):	Aplikace/Text
Group(da):	Programmer/Tekst
Group(de):	Applikationen/Text
Group(es):	Aplicaciones/Texto
Group(fr):	Applications/Texte
Group(is):	Forrit/Texti
Group(it):	Applicazioni/Testo
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•∆•≠•π•»
Group(no):	Applikasjoner/Tekst
Group(pl):	Aplikacje/Tekst
Group(pt):	AplicaÁıes/Texto
Group(ru):	“…Ãœ÷≈Œ…—/Ù≈À”‘œ◊Ÿ≈ ’‘…Ã…‘Ÿ
Group(sl):	Programi/Besedilo
Group(sv):	Till‰mpningar/Text
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/Ù≈À”‘œ◊¶ ’‘…Ã¶‘…
Vendor:		Caolan McNamara <Caolan.McNamara@ul.ie>
Source0:	http://download.sourceforge.net/wvware/%{name}-%{version}.tar.gz
Patch0:		%{name}-magick.patch
URL:		http://www.wvWare.com/
BuildRequires:	XFree86-devel
BuildRequires:	ImageMagick-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRequires:	libwmf-devel >= 0.2.1
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
Group(cs):	V˝vojovÈ prost¯edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	ﬁrÛunartÛl/Agerasˆfn
Group(it):	Sviluppo/Librerie
Group(ja):	≥´»Ø/•È•§•÷•È•Í
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(sl):	Razvoj/Knjiænice
Group(sv):	Utveckling/Bibliotek
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Contains the header files.

%description devel -l pl
Pakiet tem zawiera pliki nag≥Ûwkowe wv.

%package static
Summary:	Static wv libraries
Summary(pl):	Biblioteki statyczne wv
Summary(pt_BR):	Bibliotecas est·ticas para desenvolvimento com o wv
Group:		Libraries
Group(cs):	Knihovny
Group(da):	Biblioteker
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(is):	Agerasˆfn
Group(it):	Librerie
Group(ja):	•È•§•÷•È•Í
Group(no):	Biblioteker
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(sl):	Knjiænice
Group(sv):	Bibliotek
Group(uk):	‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Contains static wv libraries.

%description static -l pl
Pakiet zawiera statyczne biblioteki wv.

%prep
%setup -q
%patch0 -p1

# Checking for CVS specific files and removing them.
find . -type d -name 'CVS'| xargs rm -rf

%build
rm -f missing acinclude.m4
libtoolize --copy --force
aclocal
autoconf
autoheader
automake -a -c -i
CPPFLAGS="-I/usr/X11R6/include/X11"; export CPPFLAGS
%configure \
	--with-exporter \
	--with-zlib \
	--with-png \
	--with-expat \
	--with-libwmf \
	--with-Magick=/usr/X11R6 \
	--enable-static

mv -f magick magick-wv
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir}/man1

gzip -9nf CHANGELOG CREDITS D_CREDITS D_README KNOWN-BUGS README TESTING TODO.TXT

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/wv*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/wv
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libwv-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libwv.a

Summary:	MSWord Document to HTML converter
Summary(pl):	Konwerter domumentów MSWord do HTML
Name:		wv
Version:	0.6.2
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
Pakiet tem zawiera pliki nag³ówkowe

%package static
Summary:	Static libraries
Summary(pl):	Biblioteki statyczne
Group:		Libraries
Group(de):	Libraries
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
if [ -d ./CVS ]; then
	for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
		if [ -e "$i" ]; then rm -r -f $i; fi
	done
fi

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf helper-scripts/*

%clean
# rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc helper-scripts
%attr(755,root,root) %{_bindir}/*
%{_libdir}/wv
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libwv.a

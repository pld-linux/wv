Summary:	MSWord Document to HTML converter
Summary(pl):	Konwerter domumentów MSWord do HTML
Name:		wv
Version:	0.5.40
Release:	3
License:	GPL
Group:		Utilities/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Narzêdzia/Tekst
Vendor:		Caolan McNamara <Caolan.McNamara@ul.ie>
Source0:	http://www.csn.ul.ie/~caolan/publink/mswordview/development/%{name}-%{version}.tar.bz2
Patch0:		wv-DESTDIR.patch
URL:		http://www.csn.ul.ie/~caolan/docs/MSWordView.html
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
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-static = %{version}

%description devel
Contains the header files.

%description -l pl devel
Pakiet tem zawiera pliki nag³ówkowe

%package static
Summary:	Static libraries
Summary(pl):	Biblioteki statyczne
Group:		Libraries
Group(pl):	Biblioteki
#????Requires:%{name} = %{version}

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
		if [ -e "$i" ]; then rm -r $i; fi
	done
fi

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	install

( cd $RPM_BUILD_ROOT%{_bindir}; ln -sf wvConvert wvText; ) 

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* helper-scripts/* \
	ABIWORD-SUGGESTIONS CHANGELOG CREDITS D_CREDITS D_README KNOWN-BUGS \
	README README.NEW TESTING TODO.TXT

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc helper-scripts *.gz
%attr(755,root,root) %{_bindir}/*
%{_libdir}/wv
%{_mandir}/man*/*.gz

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libwv.a

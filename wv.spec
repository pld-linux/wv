Summary:	MSWord Document to HTML converter
Name:		wv
Version:	0.5.40
Release:	2
License:	GPL
Group:		Applications/Text
Vendor:		Caolan McNamara <Caolan.McNamara@ul.ie>
Source:		%{name}-%{version}.tar.bz2
URL:		http://www.csn.ul.ie/~caolan/docs/MSWordView.html
Obsoletes:	mswordview
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MSWordView is a program that understands the Microsoft Word 8
binary file format (Office97) and is able to convert Word
documents into HTML, which can then be read with a browser.

wv is a suite of programs to help convert Word Documents to HTML.

%prep
%setup -q -n %{name}
# Checking for CVS specific files and removing them.
if [ -d ./CVS ]; then
	for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
		if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
	done
fi

%build
%configure --prefix=/usr
make

%install
rm -r $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/include

make prefix=$RPM_BUILD_ROOT/usr install

( cd $RPM_BUILD_ROOT/usr/bin; ln -sf wvConvert wvText; ) 

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc examples feature-examples gateway helper-scripts notes mswordview.lsm
%doc ABIWORD-SUGGESTIONS BIG5.TXT CHANGELOG COPYING CREDITS D_CREDITS
%doc D_README INSTALL KNOWN-BUGS README README.NEW TESTING TODO.TXT
/usr/bin/wv*
/usr/include/wv.h
/usr/lib/libwv.a
/usr/lib/wv
/usr/man/man1/wvHtml.1

%define	name	wv
%define	version	0.5.40
%define	release	2
%define	serial	1

Summary:	MSWord Document to HTML converter
Name:		%{name}
Version:	%{version}
Release:	%{release}
Serial:		%{serial}
Copyright:	GPL
Group:		Applications/Text
URL:		http://www.csn.ul.ie/~caolan/docs/MSWordView.html
Vendor:		Caolan McNamara <Caolan.McNamara@ul.ie>
Source:		%{name}-%{version}.tar.bz2
Obsoletes:	mswordview
BuildRoot:	/var/tmp/%{name}-%{version}

#Distribution:	Freshmeat RPMs
Packager:	Ryan Weaver <ryanw@infohwy.com>

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
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT ; fi
mkdir -p $RPM_BUILD_ROOT/usr/include

make prefix=$RPM_BUILD_ROOT/usr install

( cd $RPM_BUILD_ROOT/usr/bin; ln -sf wvConvert wvText; ) 

%clean
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT ; fi

%files
%defattr(-,root,root)
%doc examples feature-examples gateway helper-scripts notes mswordview.lsm
%doc ABIWORD-SUGGESTIONS BIG5.TXT CHANGELOG COPYING CREDITS D_CREDITS
%doc D_README INSTALL KNOWN-BUGS README README.NEW TESTING TODO.TXT
/usr/bin/wv*
/usr/include/wv.h
/usr/lib/libwv.a
/usr/lib/wv
/usr/man/man1/wvHtml.1

%changelog
* Thu Nov 11 1999 Peter Hanecak <hanecak@megaloman.sk>
- %configure moved to %build
- source archive changed to .bz2

* Wed Nov 10 1999 Ryan Weaver <ryanw@infohwy.com>
  [wv-0.5.40-1]
- took a patch from Mitch Davis <mjd@aus.hp.com> to change PAGESIZE to
  WV_PAGESIZE, this define already exists under HPUX (oops), and modify
  -I./ to -I. which supposedly makes a difference.
- output title in the same output charset as the rest of the document.
- inserted a hack to force lists to end before </td>, rather than
  after the </td>
- made a fix to setting the chp istd correctly after an initialization
- the style 10 (Normal) is Generated first if possible, as other styles
  (illegally i think) depend on it in the style generation code.
- tables and list were interacting badly with eachother to create invalid
  html and incorrect numbering, fixed this.
- doubled up the alignment tag with div align as well as the style 
  assignment as netscape is having problems with short paragraph alignment.
- made some changes so that the first list start no is always 1 rather 
  than programmer 0 :-).
- add a <br> as a section break to wvHtml.xml, sometimes a heading
  starts after a section break, but because of no <p> it ends up in a 
  bad position.
- hacked in some sanity checks to swap between unicode and 8bit in the
  stylesheet names, some mac docs are using 8bit names in word8 files.
- hacked in a mechanism to fake a section the size of the document if
  there are no sections in the section listing, like there always is 
  except for some strange mac word8 docs that I received.
- an attempt to make nfc's more like liststartnos so that sublists that
  start > 1 levels below the last list entry have the correct nfc code.
- forced a paraend in html mode to close off any open lists
- I wasted a *lot* of time getting multilevel lists to do exactly
  the right thing, and to get them html complient. I now submit that
  the problem is really actually quite a toughy without scanning the
  entire list before printing it (which i do do with tables ). The 
  interpretation of html lists doesnt help the matter, its *close*
  to what I want but just far enough away to be useless.
- It became necessary to duplicate the paraending code for the end of a piece 
  in the simple mode as well as complex. THe simple code is now almost exactly
  the same as the complex, ah well.
- I believe I have correctly worked out how to determine when word 6 and 7 files use 
  unicode characters.

* Wed Oct 13 1999 Ryan Weaver <ryanw@infohwy.com>
  [wv-0.5.39-1]
- made a new wvHtml conversion page, looks nice to me, online bug listing, 
  its hardly a bugzilla bug it serves better for my needs.
- added placeholder.png and wvOnline.xml to cvs, neither of which are of
  any real importance except for the interim.
- added <filename/> variable, handy for the online converter.
- added three sprms of (now) known length and unknown purpose to word7
  sprm list.
- NONE of the word documents that I have (4747 of them, 556Megs) now crash
  with the current version, this is not to say there there are not serious
  crashable bugs, or that the output is sane, just that it is now quite
  reliable.
- versioning enum extended and renumbered to handle all word formats in
  the future, hardcoded 0 and 1 changed to WORD8 and WORD6.
- finally hacked in preliminary stylesheet code to get the dependancies
  in the correct order, its a bit crufty (!), but it does the trick for
  now.

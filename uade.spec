Summary:	Replayer for old amiga music file formats
Summary(pl):	Odtwarzacz starych amigowych plików muzycznych
Name:		uade
Version:	0.70
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://www.ee.tut.fi/~heikki/uade/%{name}-%{version}.tar.bz2
URL:		http://www.ee.tut.fi/~heikki/uade.html
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr
%define		_libdir		%(xmms-config --input-plugin-dir)
%define		_datadir	%{_prefix}/share/uade

%description
UADE is a replayer for old amiga music file formats. It uses an UAE
emulation of the AMIGA Hardware and a cloned m68k-assembler Amiga
delitracker API to be able to replay those tunes again on platforms
other than the original AMIGA.

%description -l pl
UADE jest odtwarzaczem starych amigowych formatów plików muzycznych.
U¿ywa emulacji sprzêtu z UAE i sklonowanego API delitrackera, by móc
odtworzyæ ponownie te melodie na platformach innych ni¿ Amiga.

%package examples
Summary:	Sample amiga tunes
Summary(pl):	Przyk³adowe melodie
Group:		Applications/Sound

%description examples
Some sample amiga tunes you can use to test if UADE works.

%description examples -l pl
Kilka przyk³adowych amigowych melodii, które mo¿esz wykorzystaæ do
sprawdzenia, czy UADE dzia³a.

%package -n xmms-input-uade
Summary:	UADE plugin for XMMS
Summary(pl):	Plugin dla XMMS wykorzystuj±cy UADE
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description -n xmms-input-uade
For people that prefer a GUI rather than plain console apps and their
switches or those who just want to listen to their music with XMMS and
take advantage of it's features like playlists, different output,
effect and visual plugins there's also a UADE XMMS input plugin.

%description -n xmms-input-uade -l pl
Dla tych, którzy preferuj± GUI od aplikacji trybu tekstowego i ich
prze³±czników, lub po prostu chc± s³uchaæ muzyki u¿ywaj±c XMMS,
korzystaj±c z jego cech, jak playlisty, ró¿ne wyj¶cia, efekty i
pluginy wizualizacyjne, jest plugin dla XMMS korzystaj±cy z UADE.

%prep
%setup -q -n uade-%{version}

%build
%configure --prefix=%{_prefix}
cd plugindir
cat Makefile | sed 's@PLUGINDIR = @&$(DESTDIR)@' > Makefile.new
mv -f Makefile.new Makefile
cd ..
cat Makefile | sed 's@SYSDATADIR = @&$(DESTDIR)@' > Makefile.new
cat Makefile.new | sed 's@BINDIR = @&$(DESTDIR)@' > Makefile

%{__make} CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog.txt
find uade-docs -type f | xargs gzip -9nf

gzip -9nf cust/* dlm/* fc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz uade-docs/*.gz
%doc uade-docs/decrunch uade-docs/players
%attr(755,root,root) %{_bindir}/uade
%{_datadir}

%files examples
%defattr(644,root,root,755)
%doc cust/* dlm/* fc/*

%files -n xmms-input-uade
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so

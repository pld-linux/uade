%define		_pre	pre7
Summary:	Replayer for old amiga music file formats
Summary(pl):	Odtwarzacz starych amigowych plików muzycznych
Name:		uade
Version:	0.80
Release:	1.%{_pre}.1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.ee.tut.fi/~heikki/uade/pre/%{name}-%{version}-%{_pre}.tar.bz2
# Source0-md5:	5ce506d1ae3e2df4889ad291ceb9f957
URL:		http://www.ee.tut.fi/~heikki/uade.html
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	xmms-devel
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{xmms_input_plugindir}
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
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}
Requires:	xmms

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
%setup -q -n %{name}-%{version}-%{_pre}

%build
./configure \
	--prefix=%{_prefix} \
	--package-prefix=$RPM_BUILD_ROOT \
	--input-plugin-dir=%{_libdir} \
	--with-sdl

%{__make} \
	CC="%{__cc}" \
	LIBTOOL="libtool --tag=dupa"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.txt BUGS FIXED
%doc uade-docs/decrunch uade-docs/players
%doc uade-docs/faq.html uade-docs/*.txt
%attr(755,root,root) %{_bindir}/uade
%{_datadir}

%files examples
%defattr(644,root,root,755)
%doc songs/*

%files -n xmms-input-uade
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so

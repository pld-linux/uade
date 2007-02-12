Summary:	Replayer for old amiga music file formats
Summary(pl.UTF-8):	Odtwarzacz starych amigowych plików muzycznych
Name:		uade
Version:	1.03
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://zakalwe.virtuaalipalvelin.net/uade/uade/%{name}-%{version}.tar.bz2
# Source0-md5:	97e0eed37d91bc76079e9b5ee108a5a3
URL:		http://zakalwe.virtuaalipalvelin.net/uade/
BuildRequires:	gtk+-devel
BuildRequires:	libao-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{xmms_input_plugindir}
%define		_datadir	%{_prefix}/share/uade

%description
UADE is a replayer for old amiga music file formats. It uses an UAE
emulation of the AMIGA Hardware and a cloned m68k-assembler Amiga
delitracker API to be able to replay those tunes again on platforms
other than the original AMIGA.

%description -l pl.UTF-8
UADE jest odtwarzaczem starych amigowych formatów plików muzycznych.
Używa emulacji sprzętu z UAE i sklonowanego API delitrackera, by móc
odtworzyć ponownie te melodie na platformach innych niż Amiga.

%package examples
Summary:	Sample amiga tunes
Summary(pl.UTF-8):	Przykładowe melodie
Group:		Applications/Sound

%description examples
Some sample amiga tunes you can use to test if UADE works.

%description examples -l pl.UTF-8
Kilka przykładowych amigowych melodii, które można wykorzystać do
sprawdzenia, czy UADE działa.

%package -n xmms-input-uade
Summary:	UADE plugin for XMMS
Summary(pl.UTF-8):	Wtyczka dla XMMS-a wykorzystująca UADE
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	xmms

%description -n xmms-input-uade
For people that prefer a GUI rather than plain console apps and their
switches or those who just want to listen to their music with XMMS and
take advantage of it's features like playlists, different output,
effect and visual plugins there's also a UADE XMMS input plugin.

%description -n xmms-input-uade -l pl.UTF-8
Dla tych, którzy preferują GUI od aplikacji trybu tekstowego i ich
przełączników, lub po prostu chcą słuchać muzyki używając XMMS-a,
korzystając z jego cech, takich jak playlisty, różne wyjścia, efekty i
wtyczki wizualizacyjne, jest wtyczka dla XMMS-a korzystająca z UADE.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--package-prefix=$RPM_BUILD_ROOT \
	--xmms-plugin-dir=%{_libdir} \
	--with-ao \
	--without-alsa \
	--without-oss \
	--without-sdl \
	--without-bmp

%{__make} \
	CC="%{__cc}" \
	ARCHFLAGS="%{rpmcflags}"

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
%{_mandir}/man1/*

%files examples
%defattr(644,root,root,755)
%doc songs/*

%files -n xmms-input-uade
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so

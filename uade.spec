Summary:	Replayer for old amiga music file formats
Summary(pl):	Odtwarzacz starych amigowych plik�w muzycznych
Name:		uade
Version:	0.91
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://uade.ton.tut.fi/uade/%{name}-%{version}.tar.bz2
# Source0-md5:	3b7fa0899e3456e0d37c50048685881e
URL:		http://uade.ton.tut.fi/
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
UADE jest odtwarzaczem starych amigowych format�w plik�w muzycznych.
U�ywa emulacji sprz�tu z UAE i sklonowanego API delitrackera, by m�c
odtworzy� ponownie te melodie na platformach innych ni� Amiga.

%package examples
Summary:	Sample amiga tunes
Summary(pl):	Przyk�adowe melodie
Group:		Applications/Sound

%description examples
Some sample amiga tunes you can use to test if UADE works.

%description examples -l pl
Kilka przyk�adowych amigowych melodii, kt�re mo�esz wykorzysta� do
sprawdzenia, czy UADE dzia�a.

%package -n xmms-input-uade
Summary:	UADE plugin for XMMS
Summary(pl):	Plugin dla XMMS-a wykorzystuj�cy UADE
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}
Requires:	xmms

%description -n xmms-input-uade
For people that prefer a GUI rather than plain console apps and their
switches or those who just want to listen to their music with XMMS and
take advantage of it's features like playlists, different output,
effect and visual plugins there's also a UADE XMMS input plugin.

%description -n xmms-input-uade -l pl
Dla tych, kt�rzy preferuj� GUI od aplikacji trybu tekstowego i ich
prze��cznik�w, lub po prostu chc� s�ucha� muzyki u�ywaj�c XMMS-a,
korzystaj�c z jego cech, jak playlisty, r�ne wyj�cia, efekty i
pluginy wizualizacyjne, jest plugin dla XMMS-a korzystaj�cy z UADE.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--package-prefix=$RPM_BUILD_ROOT \
	--xmms-plugin-dir=%{_libdir} \
	--with-sdl \
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

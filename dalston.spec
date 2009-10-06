%define version 0.1.6
%define rel 1
%define snapshot git20091002
%define release %mkrel 0.%{snapshot}.%{rel}
%define sversion %{version}%{snapshot}

Name: dalston
Summary: System information icons for Moblin
Group: Graphical desktop/Other 
Version: %{version}
License: LGPL 2.1
URL: http://www.moblin.org
Release: %{release}
Source0: %{name}-%{sversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: libglib2-devel
BuildRequires: libdbus-glib-devel
BuildRequires: gtk+2-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libcanberra-devel
BuildRequires: nbtk-devel
BuildRequires: libnotify-devel
BuildRequires: libGConf2-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: mutter-moblin-devel

%description
System information icons for Moblin

%prep
%setup -q -n %{name}-%{sversion}

%build
NOCONFIGURE=foo ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%doc COPYING NEWS AUTHORS README ChangeLog
%{_sysconfdir}/xdg/autostart/*
%{_bindir}/dalston-power-applet
%{_bindir}/dalston-volume-applet
%{_bindir}/dalston-power-settings-capplet
%{_datadir}/dalston/icons/*
%{_datadir}/applications/*.desktop
%{_datadir}/dalston/theme/*
%{_datadir}/locale/*

Name: dalston
Summary: System information icons for Moblin
Group: Graphical desktop/Other 
Version: 0.1.10
License: LGPL 2.1
URL: http://www.moblin.org
Release: %mkrel 1
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
Patch0: dalston-0.1.6git20091002-powerpolicy.patch
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
BuildRequires: gnome-common
BuildRequires: moblin-panel-devel

%description
System information icons for Moblin

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .powerpolicy

%build
NOCONFIGURE=foo ./autogen.sh
%configure2_5x --enable-settings-capplet
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
%{_libexecdir}/dalston-power-applet
%{_libexecdir}/dalston-volume-applet
%{_bindir}/dalston-power-settings-capplet
%{_datadir}/dbus-1/services/org.moblin.*.service
%{_datadir}/dalston/icons/*
%{_datadir}/applications/*.desktop
%{_datadir}/dalston/theme/*
%{_datadir}/locale/*

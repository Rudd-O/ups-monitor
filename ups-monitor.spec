# $Id$

%define ver 0.8.1
%define rel 1
%define prefix /usr

Summary:        An UPS monitor for the GNOME desktop
Summary(es):	Un monitor de SAI para el escritorio GNOME
Name:           ups-monitor
Vendor:         Amauta
Version:        %ver
Release:        %rel
Copyright:      Amautacorp S.A. 
Group:          System/Monitoring
Source:         %{name}-%ver.tar.gz
URL:            http://www.amautacorp.com/staff/Rudd-O/projects/ups-front/
BuildRoot:      %{_tmppath}/build-%{name}-%{ver}
Requires:       pygtk2 pygtk2-libglade gnome-python2
BuildArch:      i386
Packager:       Manuel Amador (Rudd-O) <rudd-o@amautacorp.com>

%description
UPS monitor is a simple tool that displays UPS information in real time.
It can monitor a UPS attached to your computer, or a a network server
plugged into an UPS.

UPS monitor requires the Network UPS Tools server.


%description -l es
Monitor de SAI es una herramienta simple que muestra información sobre
su SAI (sistema de alimentación ininterrumpida, más conocido como UPS).
Usando UPS monitor, Ud. puede monitorear un SAI conectado a su PC, o
SAIs conectados a otras computadoras de la red.

Monitor de SAI necesita el servicio Network UPS Tools (nut).


%changelog
* Fri Mar 11 2005 Manuel Amador <rudd-o@amautacorp.com> 0.8.1-1
- Using GNOME support functions instead of rolling my own.
- Build system improved

* Mon Feb 07 2005  Arnaud Quette  <arnaud.quette@mgeups.com> 0.8.1-1
- Change version numbering to x.y.z (0.8.1)
- Correct eggtray install/uninstall/clean rules
- Add a basic manpage
- Add a bzdist rule to generate tar.bz2 archives
- Modified the Changelog format to be more meaningful

* Sun Jul 25 2004 Manuel Amador (Rudd-O) <rudd-o@amautacorp.com> 0.4-1
- Implemented smart tray icon
- Improved user interaction and usability
- Improvements to README, additions to TODO
- Removed GNOME dependency

* Fri Jul 23 2004 Manuel Amador (Rudd-O) <rudd-o@amautacorp.com> 0.3-1
- Credit to Eugenia
- Fixed GladeXML bug which caused remotely connected UPSes not to work
- Usability improvements in error messages and consistency in routines
- Translations in spec file
- Improvements to README, additions to TODO

* Wed Jul 21 2004 Manuel Amador (Rudd-O) <rudd-o@amautacorp.com> 0.2-1
- HIGified the UI after Eugenia Loli-Queru's suggestions

* Wed Jul 21 2004 Manuel Amador (Rudd-O) <rudd-o@amautacorp.com> 0.1-1
- spec file improvements

* Sat Jul 17 2004 Manuel Amador (Rudd-O) <rudd-o@amautacorp.com> 0.1-0
- first time RPM creation
- first release

%prep
rm -rf $RPM_BUILD_ROOT

%setup
./configure --prefix=/usr

%build

%install
make DESTDIR=$RPM_BUILD_ROOT install



%files
%defattr(-,root,root)
%prefix/bin/%name
%prefix/share/applications
%prefix/share/pixmaps/%name.png
%prefix/share/%name
%doc %prefix/man/man1/*
%doc %prefix/share/doc/%name-%ver

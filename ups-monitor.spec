# $Id: mydms.spec 57 2004-06-29 00:14:59Z rudd-o $

%define ver 0.3
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
URL:            http://www.amautacorp.com/staff/Rudd-O/ups-monitor/
BuildRoot:      %{_tmppath}/build-%{name}-%{ver}
Requires:       pygtk2 pygtk2-libglade
BuildArch:      noarch
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

%build

%install
PREFIX=%prefix make install



%files
%defattr(-,root,root)
%prefix/bin/ups-monitor
%prefix/share/applications
%prefix/share/pixmaps
%prefix/share/ups-monitor
%doc %prefix/share/doc
